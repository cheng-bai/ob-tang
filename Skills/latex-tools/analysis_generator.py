#!/usr/bin/env python3
"""
考点分析生成器 - 接入 math-master-teacher Skills
"""

import subprocess
import json
from typing import Dict, Optional


class AnalysisGenerator:
    """考点分析生成器"""
    
    def __init__(self):
        self.skill_name = "math-master-teacher"
    
    def generate_analysis(self, question_content: str, answer: str, 
                         difficulty: str) -> Optional[Dict[str, str]]:
        """
        调用 math-master-teacher Skills 生成考点分析
        
        Args:
            question_content: 题目内容
            answer: 答案
            difficulty: 难度（基础/中档/较难/压轴）
            
        Returns:
            包含考点分析的字典，或 None（如果调用失败）
        """
        prompt = f"""请作为20年教龄的省级数学特级教师，对以下上海高考数学题进行深度考点分析。

题目内容：
{question_content}

答案：{answer}

难度：{difficulty}

请提供以下分析（JSON格式）：
{{
    "核心考点": "主要考查的数学知识点",
    "难度评估": "详细分析题目难度和思维层次",
    "易错警示": "学生容易犯的错误和思维误区",
    "方法总结": "解题的关键方法和技巧",
    "教学建议": "针对教师的教学指导建议",
    "命题意图": "出题人可能的考查目的",
    "变式训练": "建议的变式题目方向"
}}

请确保分析专业、深入、有教学价值。"""
        
        try:
            # 调用 math-master-teacher Skills
            result = subprocess.run(
                ['npx', 'openskills', 'run', self.skill_name, '--prompt', prompt],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                # 解析返回的 JSON
                output = result.stdout.strip()
                # 提取 JSON 部分
                json_match = self._extract_json(output)
                if json_match:
                    return json.loads(json_match)
                else:
                    # 如果无法提取 JSON，返回原始文本
                    return {"原始分析": output}
            else:
                print(f"Skills 调用失败：{result.stderr}")
                return None
                
        except subprocess.TimeoutExpired:
            print("Skills 调用超时")
            return None
        except Exception as e:
            print(f"Skills 调用异常：{e}")
            return None
    
    def _extract_json(self, text: str) -> Optional[str]:
        """从文本中提取 JSON"""
        # 尝试找到 JSON 对象
        start = text.find('{')
        end = text.rfind('}')
        if start != -1 and end != -1 and end > start:
            return text[start:end+1]
        return None
    
    def format_analysis(self, analysis: Dict[str, str]) -> str:
        """格式化考点分析为 MD"""
        sections = []
        
        for key, value in analysis.items():
            if value:
                sections.append(f"【{key}】{value}")
        
        return '\n'.join(sections)


# 备用：本地规则生成（当 Skills 不可用时）
class LocalAnalysisGenerator:
    """本地规则考点分析生成器"""
    
    def __init__(self):
        self.knowledge_points = {
            '集合': ['集合运算', '子集', '交集并集'],
            '函数': ['函数性质', '单调性', '奇偶性', '最值'],
            '三角': ['三角函数', '三角恒等变换', '解三角形'],
            '数列': ['等差数列', '等比数列', '数列求和'],
            '向量': ['平面向量', '数量积', '向量运算'],
            '立体': ['空间几何', '线面关系', '空间向量'],
            '解析': ['直线圆', '椭圆', '双曲线', '抛物线'],
            '导数': ['导数运算', '函数单调性', '极值最值'],
            '概率': ['古典概型', '条件概率', '分布列'],
        }
    
    def generate_analysis(self, question_content: str, answer: str,
                         difficulty: str) -> Dict[str, str]:
        """基于规则生成考点分析"""
        
        # 识别知识点
        found_knowledge = []
        for keyword, points in self.knowledge_points.items():
            if keyword in question_content:
                found_knowledge.extend(points)
        
        # 根据难度生成分析
        difficulty_analysis = {
            '基础': '本题为基础题，主要考查基本概念和公式应用，计算量较小。',
            '中档': '本题为中档题，需要综合运用多个知识点，有一定的思维量和计算量。',
            '较难': '本题为较难题，考查深度理解和灵活应用，需要较强的分析能力。',
            '压轴': '本题为压轴题，综合性强，思维难度大，考查学生的数学素养和创新能力。'
        }.get(difficulty, '难度适中。')
        
        return {
            '核心考点': '、'.join(found_knowledge[:3]) if found_knowledge else '待分析',
            '难度评估': difficulty_analysis,
            '易错警示': '注意审题，仔细计算，避免粗心错误。',
            '方法总结': '根据题目特征选择合适的方法，规范书写解题过程。',
            '教学建议': '建议学生掌握基本方法，多做同类题巩固。',
        }


def generate_analysis_for_question(question: dict, use_skills: bool = True) -> str:
    """
    为题目生成考点分析
    
    Args:
        question: 题目字典
        use_skills: 是否使用 math-master-teacher Skills
        
    Returns:
        格式化后的考点分析文本
    """
    content = '\n'.join(question.get('content', []))
    answer = question.get('answer', '')
    difficulty = question.get('difficulty', '中档')
    
    if use_skills:
        generator = AnalysisGenerator()
        analysis = generator.generate_analysis(content, answer, difficulty)
        if analysis:
            return generator.format_analysis(analysis)
    
    # 降级到本地生成
    generator = LocalAnalysisGenerator()
    analysis = generator.generate_analysis(content, answer, difficulty)
    return '\n'.join([f"【{k}】{v}" for k, v in analysis.items()])


if __name__ == '__main__':
    # 测试
    test_question = {
        'content': ['已知函数 $f(x) = x^3 - 3x$，求其单调区间。'],
        'answer': '单调递增区间：$(-\infty, -1)$ 和 $(1, +\infty)$；单调递减区间：$(-1, 1)$',
        'difficulty': '中档'
    }
    
    print("测试本地生成：")
    result = generate_analysis_for_question(test_question, use_skills=False)
    print(result)
