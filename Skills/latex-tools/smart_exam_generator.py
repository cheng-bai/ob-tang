#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能组卷系统 - Smart Exam Generator
功能：根据知识点、难度要求、题目数量智能生成试卷方案
作者：AI Assistant
版本：1.0.0
"""

import json
import random
import argparse
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Tuple
from enum import Enum
from pathlib import Path


class DifficultyLevel(Enum):
    """难度等级"""
    EASY = 1      # 基础题
    MEDIUM = 2    # 中等题
    HARD = 3      # 难题
    EXPERT = 4    # 压轴题


class QuestionType(Enum):
    """题目类型"""
    SINGLE_CHOICE = "单选题"
    MULTI_CHOICE = "多选题"
    FILL_BLANK = "填空题"
    CALCULATION = "计算题"
    PROOF = "证明题"
    APPLICATION = "应用题"


@dataclass
class Question:
    """题目数据结构"""
    id: str
    title: str
    type: QuestionType
    difficulty: DifficultyLevel
    knowledge_points: List[str]
    score: float
    source_paper: str
    similar_questions: List[str] = field(default_factory=list)
    variation_level: int = 0  # 0=基础题, 1=变式1, 2=变式2...
    parent_question: Optional[str] = None  # 父题ID
    similarity_scores: Dict[str, float] = field(default_factory=dict)  # 相似度评分
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "type": self.type.value,
            "difficulty": self.difficulty.value,
            "knowledge_points": self.knowledge_points,
            "score": self.score,
            "source_paper": self.source_paper,
            "similar_questions": self.similar_questions,
            "variation_level": self.variation_level,
            "parent_question": self.parent_question,
            "similarity_scores": self.similarity_scores
        }


@dataclass
class ExamPaper:
    """试卷数据结构"""
    id: str
    name: str
    region: str
    year: int
    questions: List[Question] = field(default_factory=list)
    total_score: float = 0.0
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "region": self.region,
            "year": self.year,
            "total_score": self.total_score,
            "questions": [q.to_dict() for q in self.questions]
        }


@dataclass
class ExamPlan:
    """组卷方案"""
    plan_id: str
    target_knowledge: List[str]
    target_difficulty: DifficultyLevel
    total_questions: int
    selected_questions: List[Question] = field(default_factory=list)
    papers_used: List[str] = field(default_factory=list)
    coverage_score: float = 0.0  # 知识点覆盖率
    difficulty_match: float = 0.0  # 难度匹配度
    
    def to_dict(self) -> dict:
        return {
            "plan_id": self.plan_id,
            "target_knowledge": self.target_knowledge,
            "target_difficulty": self.target_difficulty.value,
            "total_questions": self.total_questions,
            "coverage_score": self.coverage_score,
            "difficulty_match": self.difficulty_match,
            "papers_used": self.papers_used,
            "selected_questions": [q.to_dict() for q in self.selected_questions]
        }


class QuestionGraph:
    """题目关系图谱管理"""
    
    def __init__(self, graph_path: str):
        self.graph_path = graph_path
        self.questions: Dict[str, Question] = {}
        self.similarity_matrix: Dict[str, Dict[str, float]] = {}
        self.variation_chains: Dict[str, List[str]] = {}  # 变式题链
        self.load_graph()
    
    def load_graph(self):
        """加载题目关系图谱"""
        try:
            with open(self.graph_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # 加载题目
            for q_data in data.get("questions", []):
                question = Question(
                    id=q_data["id"],
                    title=q_data["title"],
                    type=QuestionType(q_data["type"]),
                    difficulty=DifficultyLevel(q_data["difficulty"]),
                    knowledge_points=q_data["knowledge_points"],
                    score=q_data["score"],
                    source_paper=q_data["source_paper"],
                    similar_questions=q_data.get("similar_questions", []),
                    variation_level=q_data.get("variation_level", 0),
                    parent_question=q_data.get("parent_question"),
                    similarity_scores=q_data.get("similarity_scores", {})
                )
                self.questions[q_data["id"]] = question
            
            # 加载相似度矩阵
            self.similarity_matrix = data.get("similarity_matrix", {})
            
            # 构建变式题链
            self._build_variation_chains()
            
            print(f"✓ 加载了 {len(self.questions)} 道题目")
        except FileNotFoundError:
            print(f"⚠ 图谱文件不存在: {self.graph_path}")
            self._init_sample_data()
    
    def _init_sample_data(self):
        """初始化示例数据"""
        sample_questions = [
            Question("Q001", "一元二次方程求解", QuestionType.CALCULATION, 
                    DifficultyLevel.EASY, ["一元二次方程", "求根公式"], 5, "2024北京中考"),
            Question("Q002", "一元二次方程应用题", QuestionType.APPLICATION,
                    DifficultyLevel.MEDIUM, ["一元二次方程", "应用题"], 8, "2024上海中考"),
            Question("Q003", "一元二次方程综合题", QuestionType.CALCULATION,
                    DifficultyLevel.HARD, ["一元二次方程", "函数"], 12, "2024广东中考"),
        ]
        for q in sample_questions:
            self.questions[q.id] = q
    
    def _build_variation_chains(self):
        """构建变式题链"""
        for qid, question in self.questions.items():
            if question.variation_level == 0:
                chain = [qid]
                current = qid
                while True:
                    # 找下一级变式
                    next_var = None
                    for qid2, q2 in self.questions.items():
                        if q2.parent_question == current:
                            next_var = qid2
                            break
                    if next_var:
                        chain.append(next_var)
                        current = next_var
                    else:
                        break
                if len(chain) > 1:
                    self.variation_chains[qid] = chain
    
    def get_similar_questions(self, question_id: str, threshold: float = 0.7) -> List[Tuple[str, float]]:
        """获取相似题目（相似度>=阈值）"""
        if question_id not in self.similarity_matrix:
            return []
        
        similarities = self.similarity_matrix[question_id]
        return [(qid, score) for qid, score in similarities.items() if score >= threshold]
    
    def get_variation_chain(self, question_id: str) -> List[str]:
        """获取变式题链"""
        # 找到根节点
        root = question_id
        while self.questions[root].parent_question:
            root = self.questions[root].parent_question
        
        return self.variation_chains.get(root, [question_id])
    
    def find_questions_by_knowledge(self, knowledge_points: List[str]) -> List[Question]:
        """根据知识点查找题目"""
        results = []
        for question in self.questions.values():
            if any(kp in question.knowledge_points for kp in knowledge_points):
                results.append(question)
        return results
    
    def calculate_similarity(self, q1: Question, q2: Question) -> float:
        """计算两题相似度（基于知识点重叠）"""
        kp1 = set(q1.knowledge_points)
        kp2 = set(q2.knowledge_points)
        
        if not kp1 or not kp2:
            return 0.0
        
        intersection = len(kp1 & kp2)
        union = len(kp1 | kp2)
        
        return intersection / union if union > 0 else 0.0


class SmartExamGenerator:
    """智能组卷生成器"""
    
    def __init__(self, graph_path: str):
        self.graph = QuestionGraph(graph_path)
        self.exam_papers: Dict[str, ExamPaper] = {}
    
    def add_exam_paper(self, paper: ExamPaper):
        """添加试卷到题库"""
        self.exam_papers[paper.id] = paper
    
    def generate_exam_plan(
        self,
        knowledge_points: List[str],
        difficulty: DifficultyLevel,
        total_questions: int,
        question_types: Optional[List[QuestionType]] = None,
        avoid_similar: bool = True,
        coverage_weight: float = 0.6,
        difficulty_weight: float = 0.4
    ) -> ExamPlan:
        """
        生成组卷方案
        
        Args:
            knowledge_points: 目标知识点列表
            difficulty: 目标难度
            total_questions: 题目数量
            question_types: 题目类型限制（可选）
            avoid_similar: 是否避免选择相似题
            coverage_weight: 知识点覆盖率权重
            difficulty_weight: 难度匹配度权重
        """
        plan_id = f"PLAN_{random.randint(1000, 9999)}"
        
        # 1. 筛选符合知识点的题目
        candidates = self.graph.find_questions_by_knowledge(knowledge_points)
        
        if question_types:
            candidates = [q for q in candidates if q.type in question_types]
        
        if not candidates:
            print(f"⚠ 未找到符合条件的题目")
            return ExamPlan(plan_id, knowledge_points, difficulty, total_questions)
        
        # 2. 评分排序
        scored_candidates = []
        for question in candidates:
            # 知识点覆盖率得分
            kp_match = len(set(question.knowledge_points) & set(knowledge_points))
            coverage_score = kp_match / len(knowledge_points)
            
            # 难度匹配得分（越接近目标难度得分越高）
            diff_diff = abs(question.difficulty.value - difficulty.value)
            difficulty_score = 1.0 - (diff_diff / 3.0)  # 归一化到0-1
            
            # 综合得分
            total_score = (coverage_weight * coverage_score + 
                          difficulty_weight * difficulty_score)
            
            scored_candidates.append((question, total_score, coverage_score, difficulty_score))
        
        # 按得分排序
        scored_candidates.sort(key=lambda x: x[1], reverse=True)
        
        # 3. 选择题目（考虑相似题避免）
        selected = []
        papers_used = set()
        used_similar_groups = set()
        
        for question, total_score, cov_score, diff_score in scored_candidates:
            if len(selected) >= total_questions:
                break
            
            # 检查是否应跳过（相似题避免）
            if avoid_similar:
                similar_group = tuple(sorted(self.graph.get_variation_chain(question.id)))
                if similar_group in used_similar_groups:
                    continue
                used_similar_groups.add(similar_group)
            
            selected.append(question)
            papers_used.add(question.source_paper)
        
        # 4. 计算方案指标
        if selected:
            all_kp_covered = set()
            for q in selected:
                all_kp_covered.update(q.knowledge_points)
            
            coverage_score = len(all_kp_covered & set(knowledge_points)) / len(knowledge_points)
            
            avg_difficulty = sum(q.difficulty.value for q in selected) / len(selected)
            difficulty_match = 1.0 - abs(avg_difficulty - difficulty.value) / 3.0
        else:
            coverage_score = 0.0
            difficulty_match = 0.0
        
        plan = ExamPlan(
            plan_id=plan_id,
            target_knowledge=knowledge_points,
            target_difficulty=difficulty,
            total_questions=total_questions,
            selected_questions=selected,
            papers_used=list(papers_used),
            coverage_score=coverage_score,
            difficulty_match=difficulty_match
        )
        
        return plan
    
    def generate_variation_paper(
        self,
        base_question_id: str,
        num_variations: int = 3
    ) -> List[Question]:
        """
        基于基础题生成变式题组
        
        Args:
            base_question_id: 基础题ID
            num_variations: 需要生成的变式数量
        """
        if base_question_id not in self.graph.questions:
            print(f"⚠ 未找到基础题: {base_question_id}")
            return []
        
        base_question = self.graph.questions[base_question_id]
        
        # 获取相似题
        similar = self.graph.get_similar_questions(base_question_id, threshold=0.5)
        
        # 获取变式链
        variation_chain = self.graph.get_variation_chain(base_question_id)
        
        # 组合结果
        result = [base_question]
        
        # 添加变式题
        for vid in variation_chain[1:]:
            if len(result) >= num_variations + 1:
                break
            result.append(self.graph.questions[vid])
        
        # 如果变式不够，添加相似题
        if len(result) < num_variations + 1:
            for qid, score in similar:
                if qid not in [q.id for q in result]:
                    result.append(self.graph.questions[qid])
                    if len(result) >= num_variations + 1:
                        break
        
        return result
    
    def export_plan(self, plan: ExamPlan, output_path: str):
        """导出组卷方案到JSON"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(plan.to_dict(), f, ensure_ascii=False, indent=2)
        print(f"✓ 组卷方案已导出: {output_path}")
    
    def print_plan(self, plan: ExamPlan):
        """打印组卷方案详情"""
        print("\n" + "="*60)
        print(f"📋 组卷方案: {plan.plan_id}")
        print("="*60)
        print(f"目标知识点: {', '.join(plan.target_knowledge)}")
        print(f"目标难度: {plan.target_difficulty.name}")
        print(f"题目数量: {plan.total_questions}")
        print(f"知识点覆盖率: {plan.coverage_score:.1%}")
        print(f"难度匹配度: {plan.difficulty_match:.1%}")
        print(f"引用试卷: {', '.join(plan.papers_used)}")
        print("-"*60)
        print("选题详情:")
        for i, q in enumerate(plan.selected_questions, 1):
            print(f"  {i}. [{q.type.value}] {q.title}")
            print(f"     难度: {'⭐' * q.difficulty.value} | 分值: {q.score} | 来源: {q.source_paper}")
            print(f"     知识点: {', '.join(q.knowledge_points)}")
        print("="*60)


def main():
    """主函数 - 命令行接口"""
    parser = argparse.ArgumentParser(description='智能组卷系统')
    parser.add_argument('--graph', '-g', type=str, 
                       default='/Users/tangchengbaiair/Downloads/mini-数学资料库/00-索引与配置/题目关系图谱.json',
                       help='题目关系图谱路径')
    parser.add_argument('--knowledge', '-k', type=str, nargs='+', required=False,
                       default=["一元二次方程"],
                       help='目标知识点列表')
    parser.add_argument('--difficulty', '-d', type=int, default=2,
                       choices=[1, 2, 3, 4],
                       help='难度等级 (1=基础, 2=中等, 3=难题, 4=压轴)')
    parser.add_argument('--count', '-c', type=int, default=5,
                       help='题目数量')
    parser.add_argument('--output', '-o', type=str,
                       help='输出JSON文件路径')
    parser.add_argument('--demo', action='store_true',
                       help='运行演示模式')
    
    args = parser.parse_args()
    
    # 初始化生成器
    generator = SmartExamGenerator(args.graph)
    
    if args.demo:
        # 演示模式
        print("🎯 智能组卷系统 - 演示模式\n")
        
        # 示例1: 基础组卷
        print("\n【示例1】一元二次方程基础组卷")
        plan1 = generator.generate_exam_plan(
            knowledge_points=["一元二次方程", "求根公式"],
            difficulty=DifficultyLevel.EASY,
            total_questions=3
        )
        generator.print_plan(plan1)
        
        # 示例2: 综合组卷
        print("\n【示例2】函数综合组卷")
        plan2 = generator.generate_exam_plan(
            knowledge_points=["函数", "二次函数", "图像"],
            difficulty=DifficultyLevel.MEDIUM,
            total_questions=5
        )
        generator.print_plan(plan2)
        
        # 示例3: 变式题组
        print("\n【示例3】变式题组生成")
        variations = generator.generate_variation_paper("Q001", num_variations=2)
        print(f"基础题变式组 (共{len(variations)}题):")
        for i, q in enumerate(variations, 1):
            print(f"  {i}. [{q.type.value}] {q.title} (变式等级: {q.variation_level})")
    
    else:
        # 正常模式
        difficulty = DifficultyLevel(args.difficulty)
        
        plan = generator.generate_exam_plan(
            knowledge_points=args.knowledge,
            difficulty=difficulty,
            total_questions=args.count
        )
        
        generator.print_plan(plan)
        
        if args.output:
            generator.export_plan(plan, args.output)


if __name__ == "__main__":
    main()
