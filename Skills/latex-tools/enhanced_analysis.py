#!/usr/bin/env python3
"""
增强版考点分析生成器
基于 maki 原版样式，为每道题生成深度考点分析
"""

import re
import json

class EnhancedAnalysisGenerator:
    """为试卷题目生成深度考点分析"""
    
    # 上海高考数学知识点库
    KNOWLEDGE_POINTS = {
        '集合': ['集合运算', '集合关系', '充要条件'],
        '复数': ['复数运算', '复数模', '复数几何意义'],
        '数列': ['等差数列', '等比数列', '数列求和', '递推公式'],
        '三角': ['三角函数', '三角恒等变换', '解三角形', '三角函数图像'],
        '向量': ['向量运算', '向量坐标', '向量数量积', '向量几何应用'],
        '立体几何': ['空间位置关系', '空间角', '空间距离', '空间向量'],
        '解析几何': ['直线', '圆', '椭圆', '双曲线', '抛物线', '圆锥曲线综合'],
        '函数': ['函数性质', '函数图像', '函数零点', '函数最值'],
        '导数': ['导数运算', '导数应用', '极值最值', '不等式证明'],
        '概率统计': ['概率计算', '分布列', '统计量', '回归分析'],
        '计数原理': ['排列组合', '二项式定理'],
    }
    
    # 难度评估标准
    DIFFICULTY_CRITERIA = {
        '基础': {
            '题号': [1, 2, 3, 4, 5, 6],
            '特征': ['直接计算', '公式应用', '概念理解'],
            '时间': '2-3分钟',
            '得分率': '>80%'
        },
        '中档': {
            '题号': [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
            '特征': ['多知识点综合', '需要转化', '常见题型'],
            '时间': '5-8分钟',
            '得分率': '50-80%'
        },
        '较难': {
            '题号': [19, 20],
            '特征': ['多步骤推理', '创新情境', '综合应用'],
            '时间': '12-15分钟',
            '得分率': '30-50%'
        },
        '压轴': {
            '题号': [21],
            '特征': ['高阶思维', '多方法可选', '区分度高'],
            '时间': '15-20分钟',
            '得分率': '<30%'
        }
    }
    
    def __init__(self):
        self.analysis_cache = {}
    
    def analyze_question(self, q_num, content, answer, difficulty=None):
        """
        分析单道题目，生成深度考点分析
        
        Args:
            q_num: 题号
            content: 题目内容
            answer: 答案
            difficulty: 预设难度（可选）
        
        Returns:
            dict: 包含完整考点分析的字典
        """
        # 自动判断难度
        if difficulty is None:
            difficulty = self._auto_difficulty(q_num)
        
        # 识别知识点
        knowledge = self._identify_knowledge(content)
        
        # 识别考查能力
        abilities = self._identify_abilities(content, difficulty)
        
        # 生成教学建议
        teaching_tips = self._generate_teaching_tips(knowledge, difficulty, content)
        
        # 生成易错点
        pitfalls = self._identify_pitfalls(content, answer)
        
        # 生成变式建议
        variations = self._suggest_variations(knowledge, difficulty)
        
        return {
            '题号': q_num,
            '难度': difficulty,
            '知识点': knowledge,
            '考查能力': abilities,
            '易错点': pitfalls,
            '教学建议': teaching_tips,
            '变式建议': variations,
            '预计用时': self.DIFFICULTY_CRITERIA[difficulty]['时间'],
            '目标得分率': self.DIFFICULTY_CRITERIA[difficulty]['得分率']
        }
    
    def _auto_difficulty(self, q_num):
        """根据题号自动判断难度"""
        for level, info in self.DIFFICULTY_CRITERIA.items():
            if q_num in info['题号']:
                return level
        return '中档'
    
    def _identify_knowledge(self, content):
        """识别题目涉及的知识点"""
        knowledge = []
        content_lower = content.lower()
        
        for category, points in self.KNOWLEDGE_POINTS.items():
            if category in content or category in content_lower:
                for point in points:
                    if point in content or point in content_lower:
                        knowledge.append(f"{category}-{point}")
                        break
                else:
                    knowledge.append(category)
        
        # 如果没有识别到，根据关键词推断
        if not knowledge:
            if 'sin' in content or 'cos' in content or 'tan' in content:
                knowledge.append('三角-三角函数')
            elif 'f(x)' in content or '函数' in content:
                knowledge.append('函数-函数性质')
            elif '导' in content or "f'" in content:
                knowledge.append('导数-导数应用')
            elif '向量' in content or '\overrightarrow' in content:
                knowledge.append('向量-向量运算')
            elif '椭圆' in content or '双曲线' in content or '抛物线' in content:
                knowledge.append('解析几何-圆锥曲线')
        
        return knowledge if knowledge else ['综合应用']
    
    def _identify_abilities(self, content, difficulty):
        """识别考查的数学能力"""
        abilities = ['运算求解能力']
        
        if '证明' in content:
            abilities.append('推理论证能力')
        if '如图' in content or '图像' in content:
            abilities.append('空间想象能力')
        if '应用' in content or '实际' in content:
            abilities.append('数学建模能力')
        if difficulty in ['较难', '压轴']:
            abilities.append('综合分析能力')
            abilities.append('创新应用能力')
        
        return abilities
    
    def _identify_pitfalls(self, content, answer):
        """识别常见易错点"""
        pitfalls = []
        
        if '定义域' in content or '定义域' not in content and '函数' in content:
            pitfalls.append('忽略定义域限制')
        if '等比' in content:
            pitfalls.append('等比数列公比为1的情况')
        if '三角' in content or 'sin' in content:
            pitfalls.append('三角函数符号判断错误')
        if '向量' in content:
            pitfalls.append('向量夹角范围理解错误')
        if '导数' in content:
            pitfalls.append('极值点与导数零点混淆')
        if '圆锥曲线' in content or '椭圆' in content:
            pitfalls.append('焦点位置分类讨论遗漏')
        
        return pitfalls if pitfalls else ['计算粗心']
    
    def _generate_teaching_tips(self, knowledge, difficulty, content):
        """生成教学建议"""
        tips = []
        
        if difficulty == '基础':
            tips.append('强调基本概念和公式的准确记忆')
            tips.append('训练计算准确性和速度')
        elif difficulty == '中档':
            tips.append('加强知识点之间的联系和转化')
            tips.append('总结常见题型和解题套路')
            tips.append('培养学生审题和提取信息的能力')
        elif difficulty == '较难':
            tips.append('训练多步骤问题的分解能力')
            tips.append('强调数学思想的运用（数形结合、分类讨论等）')
            tips.append('培养学生分析问题和选择策略的能力')
        else:  # 压轴
            tips.append('鼓励学生尝试多种解法')
            tips.append('训练复杂情境下的数学建模')
            tips.append('强调思维的灵活性和创造性')
        
        # 根据知识点添加具体建议
        if '导数' in str(knowledge):
            tips.append('导数问题优先考虑定义域')
        if '圆锥曲线' in str(knowledge):
            tips.append('解析几何问题优先考虑几何性质')
        if '数列' in str(knowledge):
            tips.append('数列问题注意首项和公比的验证')
        
        return tips
    
    def _suggest_variations(self, knowledge, difficulty):
        """建议变式训练方向"""
        variations = []
        
        if difficulty == '基础':
            variations.append('改变数字或条件，保持结构不变')
            variations.append('增加一步简单的逆向思维')
        elif difficulty == '中档':
            variations.append('改变问题情境，保持数学模型不变')
            variations.append('增加一个干扰条件')
            variations.append('改为开放性问题')
        else:
            variations.append('与其他知识点综合')
            variations.append('改为探索性问题')
            variations.append('增加实际应用背景')
        
        return variations
    
    def generate_latex_analysis(self, analysis):
        """生成 LaTeX 格式的考点分析"""
        latex = []
        
        # 使用 maki 原版的 analysisbox 环境
        latex.append("\\begin{analysisbox}{考点分析}")
        latex.append("  \\textbf{知识点：}" + "、".join(analysis['知识点']) + "\\par")
        latex.append("  \\textbf{考查能力：}" + "、".join(analysis['考查能力']) + "\\par")
        latex.append("  \\textbf{预计用时：}" + analysis['预计用时'] + "\\par")
        latex.append("  \\textbf{目标得分率：}" + analysis['目标得分率'])
        latex.append("\\end{analysisbox}")
        
        # 易错点提示
        if analysis['易错点']:
            latex.append("\\begin{tipbox}{易错警示}")
            for i, pitfall in enumerate(analysis['易错点'], 1):
                latex.append(f"  {i}. {pitfall}")
            latex.append("\\end{tipbox}")
        
        # 教学建议
        latex.append("\\begin{tipbox}{教学建议}")
        for tip in analysis['教学建议']:
            latex.append(f"  • {tip}")
        latex.append("\\end{tipbox}")
        
        return "\n".join(latex)


# 使用示例
if __name__ == "__main__":
    generator = EnhancedAnalysisGenerator()
    
    # 测试第 7 题（中档题）
    analysis = generator.analyze_question(
        q_num=7,
        content="已知函数 $f(x)=\\sin(\\omega x+\\varphi)$ 的最小正周期为 $\\pi$...",
        answer="$\\pi$",
        difficulty="中档"
    )
    
    print(json.dumps(analysis, ensure_ascii=False, indent=2))
    print("\n" + "="*60)
    print(generator.generate_latex_analysis(analysis))
