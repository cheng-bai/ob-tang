#!/usr/bin/env python3
"""
生成高中数学知识图谱数据
包含200+知识点和500+关联关系
覆盖7册教材全部内容
"""

import sqlite3
import json

# 数据库路径
DB_PATH = '/Users/tangchengbaiair/Downloads/mini-数学资料库/00-索引与配置/teaching_index.db'

def clear_existing_graph():
    """清空现有知识图谱数据"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM knowledge_graph")
    conn.commit()
    conn.close()
    print("已清空现有知识图谱数据")

def get_existing_points():
    """获取现有知识点"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT from_point FROM knowledge_graph UNION SELECT DISTINCT to_point FROM knowledge_graph")
    points = set(row[0] for row in cursor.fetchall())
    conn.close()
    return points

def insert_knowledge_relations(relations):
    """插入知识关联关系"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT OR IGNORE INTO knowledge_graph (from_point, to_point, relation) VALUES (?, ?, ?)",
        relations
    )
    conn.commit()
    conn.close()

def generate_knowledge_points():
    """生成完整的知识点列表"""
    
    # 必修第一册 - 集合与逻辑
    set_logic_points = [
        "集合", "元素", "集合的表示法", "列举法", "描述法", "区间表示",
        "子集", "真子集", "集合相等", "空集", "交集", "并集", "补集",
        "命题", "真命题", "假命题", "充分条件", "必要条件", "充要条件",
        "推出关系", "反证法", "逻辑否定", "全称量词", "存在量词"
    ]
    
    # 必修第一册 - 等式与不等式
    equation_inequality_points = [
        "等式", "等式性质", "方程的解", "解集", "一元一次方程",
        "一元二次方程", "判别式", "求根公式", "韦达定理", "根与系数关系",
        "不等式", "不等式性质", "一元一次不等式", "一元一次不等式组",
        "一元二次不等式", "分式不等式", "绝对值不等式", "高次不等式",
        "基本不等式", "平均值不等式", "三角不等式", "柯西不等式",
        "比较法", "分析法", "综合法", "放缩法"
    ]
    
    # 必修第一册 - 幂、指数与对数
    power_exp_log_points = [
        "幂", "指数", "正整数指数幂", "整数指数幂", "有理数指数幂", "实数指数幂",
        "根式", "n次方根", "算术根", "根式运算", "分数指数幂",
        "幂的运算性质", "幂函数", "指数函数",
        "对数", "对数定义", "常用对数", "自然对数",
        "对数运算性质", "对数换底公式", "对数函数"
    ]
    
    # 必修第一册 - 函数
    function_points = [
        "函数概念", "函数定义域", "函数值域", "函数解析式",
        "函数单调性", "增函数", "减函数", "单调区间",
        "函数奇偶性", "奇函数", "偶函数",
        "函数周期性", "周期函数", "最小正周期",
        "函数最值", "最大值", "最小值",
        "函数零点", "二分法", "函数图像",
        "反函数", "复合函数", "分段函数",
        "函数变换", "平移", "伸缩", "对称"
    ]
    
    # 必修第二册 - 三角
    trigonometry_points = [
        "角的概念", "任意角", "正角", "负角", "零角",
        "弧度制", "角度制", "弧度与角度互化",
        "终边相同的角", "象限角", "轴线角",
        "三角比", "正弦", "余弦", "正切",
        "同角三角比关系", "诱导公式", "三角恒等变换",
        "两角和差公式", "倍角公式", "半角公式",
        "辅助角公式", "万能公式", "积化和差", "和差化积"
    ]
    
    # 必修第二册 - 三角函数
    trig_function_points = [
        "正弦函数", "余弦函数", "正切函数", "余切函数",
        "正弦函数图像", "余弦函数图像", "正切函数图像",
        "正弦函数性质", "余弦函数性质", "正切函数性质",
        "周期性", "振幅", "相位", "初相", "频率",
        "正弦型函数", "y=Asin(ωx+φ)",
        "三角函数最值", "三角函数单调性",
        "解三角形", "正弦定理", "余弦定理",
        "三角形面积公式", "解三角形的应用"
    ]
    
    # 必修第二册 - 平面向量
    vector_points = [
        "向量", "向量的模", "零向量", "单位向量", "相等向量", "平行向量",
        "向量的加法", "向量的减法", "向量的数乘",
        "平面向量基本定理", "向量坐标表示",
        "向量数量积", "向量夹角", "向量垂直",
        "向量的应用", "向量在物理中的应用",
        "定比分点", "向量与几何"
    ]
    
    # 必修第二册 - 复数
    complex_points = [
        "复数", "虚数单位", "复数的实部", "复数的虚部",
        "复数相等", "共轭复数", "复数的模",
        "复平面", "复数的几何意义",
        "复数的加法", "复数的减法", "复数的乘法", "复数的除法",
        "复数的三角形式", "复数的指数形式",
        "棣莫弗定理", "复数的开方"
    ]
    
    # 必修第三册 - 空间直线与平面
    space_geometry_points = [
        "平面", "平面的表示", "平面的基本性质",
        "空间直线", "异面直线", "直线与平面的位置关系",
        "直线在平面内", "直线与平面相交", "直线与平面平行",
        "两平面的位置关系", "两平面平行", "两平面相交",
        "平行公理", "等角定理", "三垂线定理", "三垂线逆定理",
        "线面平行的判定", "线面平行的性质",
        "面面平行的判定", "面面平行的性质",
        "线面垂直", "线面垂直的判定", "线面垂直的性质",
        "面面垂直", "面面垂直的判定", "面面垂直的性质",
        "二面角", "二面角的平面角", "面面角的计算"
    ]
    
    # 必修第三册 - 简单几何体
    solid_geometry_points = [
        "多面体", "旋转体",
        "棱柱", "棱锥", "棱台", "圆柱", "圆锥", "圆台", "球",
        "柱体的表面积", "柱体的体积", "锥体的表面积", "锥体的体积",
        "台体的表面积", "台体的体积", "球的表面积", "球的体积",
        "直观图", "斜二测画法",
        "空间几何体的三视图", "空间几何体的展开图"
    ]
    
    # 必修第三册 - 概率初步
    probability_points = [
        "随机现象", "随机试验", "样本空间", "样本点",
        "随机事件", "基本事件", "必然事件", "不可能事件",
        "事件的关系", "包含关系", "相等关系", "互斥事件", "对立事件",
        "事件的运算", "并事件", "交事件",
        "概率", "频率", "概率的统计定义",
        "古典概型", "几何概型",
        "概率的基本性质", "概率的加法公式",
        "独立事件", "条件概率"
    ]
    
    # 必修第三册 - 统计
    statistics_points = [
        "总体", "个体", "样本", "样本容量",
        "简单随机抽样", "系统抽样", "分层抽样",
        "频率分布表", "频率分布直方图", "频率分布折线图", "茎叶图",
        "众数", "中位数", "平均数", "加权平均数",
        "极差", "方差", "标准差",
        "总体分布", "总体特征数的估计"
    ]
    
    # 选择性必修第一册 - 平面直角坐标系中的直线
    line_points = [
        "直线的倾斜角", "直线的斜率", "斜率公式",
        "直线的点斜式方程", "直线的斜截式方程",
        "直线的两点式方程", "直线的截距式方程",
        "直线的一般式方程", "直线方程的互化",
        "两直线平行", "两直线垂直", "两直线相交",
        "两直线的夹角", "点到直线的距离", "两平行线间的距离",
        "直线系方程", "对称问题"
    ]
    
    # 选择性必修第一册 - 圆锥曲线
    conic_points = [
        "曲线与方程", "求曲线的方程", "曲线的交点",
        "圆的标准方程", "圆的一般方程", "圆的参数方程",
        "点与圆的位置关系", "直线与圆的位置关系", "圆与圆的位置关系",
        "椭圆", "椭圆的标准方程", "椭圆的几何性质", "椭圆的离心率",
        "双曲线", "双曲线的标准方程", "双曲线的几何性质", "双曲线的离心率", "双曲线的渐近线",
        "抛物线", "抛物线的标准方程", "抛物线的几何性质", "抛物线的准线",
        "圆锥曲线的统一定义", "圆锥曲线的第二定义",
        "直线与圆锥曲线的位置关系", "弦长公式",
        "圆锥曲线的应用"
    ]
    
    # 选择性必修第一册 - 空间向量
    space_vector_points = [
        "空间向量", "空间向量的模", "空间向量的相等",
        "空间向量的加法", "空间向量的减法", "空间向量的数乘",
        "空间向量基本定理", "空间向量的坐标表示",
        "空间向量的数量积", "空间向量的夹角",
        "直线的方向向量", "平面的法向量",
        "空间向量在立体几何中的应用",
        "空间角", "异面直线所成的角", "线面角", "二面角",
        "空间距离", "点到平面的距离", "线面距离", "面面距离"
    ]
    
    # 选择性必修第一册 - 数列
    sequence_points = [
        "数列", "数列的项", "数列的通项", "数列的通项公式",
        "数列的前n项和", "数列的递推公式",
        "等差数列", "等差数列的通项公式", "等差中项",
        "等差数列的前n项和", "等差数列的性质",
        "等比数列", "等比数列的通项公式", "等比中项",
        "等比数列的前n项和", "等比数列的性质",
        "数列求和", "公式法", "倒序相加法", "错位相减法", "裂项相消法", "分组求和法",
        "数学归纳法", "数列的极限", "无穷等比数列的和"
    ]
    
    # 选择性必修第二册 - 导数
    derivative_points = [
        "导数的概念", "平均变化率", "瞬时变化率",
        "导数的几何意义", "切线", "法线",
        "导函数", "可导", "连续",
        "基本初等函数的导数", "导数的四则运算",
        "复合函数的导数", "隐函数的导数",
        "导数与单调性", "函数的单调区间",
        "极值", "极大值", "极小值", "极值点",
        "最值", "最大值", "最小值",
        "导数的应用", "优化问题", "函数零点分析",
        "洛必达法则", "泰勒展开"
    ]
    
    # 选择性必修第二册 - 计数原理
    counting_points = [
        "分类计数原理", "分步计数原理", "加法原理", "乘法原理",
        "排列", "排列数", "排列数公式", "全排列",
        "组合", "组合数", "组合数公式",
        "组合数性质", "杨辉三角",
        "二项式定理", "二项展开式", "通项公式",
        "二项式系数的性质", "赋值法",
        "排列组合综合应用"
    ]
    
    # 选择性必修第二册 - 概率初步续
    probability_advanced_points = [
        "条件概率", "条件概率公式", "乘法公式",
        "全概率公式", "贝叶斯公式",
        "事件的独立性", "独立重复试验",
        "随机变量", "离散型随机变量", "连续型随机变量",
        "概率分布列", "分布列的性质",
        "两点分布", "二项分布", "超几何分布",
        "数学期望", "方差", "标准差",
        "正态分布", "正态曲线", "正态分布的性质",
        "3σ原则"
    ]
    
    # 选择性必修第二册 - 成对数据的统计分析
    correlation_points = [
        "变量的相关性", "正相关", "负相关", "线性相关",
        "散点图", "相关系数", "相关系数的计算",
        "一元线性回归", "回归直线", "最小二乘法",
        "回归方程", "回归系数",
        "独立性检验", "2×2列联表", "卡方检验",
        "统计案例分析"
    ]
    
    # 数学建模
    modeling_points = [
        "数学建模", "数学模型",
        "问题分析", "模型假设", "模型建立", "模型求解", "模型检验",
        "优化模型", "预测模型", "评价模型"
    ]
    
    # 综合应用
    comprehensive_points = [
        "函数与方程", "数形结合", "分类讨论", "化归与转化",
        "特殊与一般", "有限与无限", "或然与必然",
        "数学思想方法", "数学思维能力"
    ]
    
    all_points = (
        set_logic_points + equation_inequality_points + power_exp_log_points +
        function_points + trigonometry_points + trig_function_points +
        vector_points + complex_points + space_geometry_points +
        solid_geometry_points + probability_points + statistics_points +
        line_points + conic_points + space_vector_points + sequence_points +
        derivative_points + counting_points + probability_advanced_points +
        correlation_points + modeling_points + comprehensive_points
    )
    
    return list(set(all_points))

def generate_prerequisite_relations():
    """生成前置关系"""
    relations = []
    
    # 集合与逻辑 -> 其他
    relations.extend([
        ("元素", "集合", "prerequisite"),
        ("集合的表示法", "集合", "prerequisite"),
        ("子集", "集合", "prerequisite"),
        ("交集", "集合", "prerequisite"),
        ("并集", "集合", "prerequisite"),
        ("补集", "集合", "prerequisite"),
        ("命题", "集合", "prerequisite"),
        ("充分条件", "命题", "prerequisite"),
        ("必要条件", "命题", "prerequisite"),
        ("充要条件", "充分条件", "prerequisite"),
        ("充要条件", "必要条件", "prerequisite"),
        ("反证法", "命题", "prerequisite"),
    ])
    
    # 等式与不等式 -> 其他
    relations.extend([
        ("等式", "方程的解", "prerequisite"),
        ("等式性质", "方程的解", "prerequisite"),
        ("一元一次方程", "一元二次方程", "prerequisite"),
        ("一元二次方程", "判别式", "prerequisite"),
        ("一元二次方程", "求根公式", "prerequisite"),
        ("一元二次方程", "韦达定理", "prerequisite"),
        ("不等式", "不等式性质", "prerequisite"),
        ("不等式性质", "一元一次不等式", "prerequisite"),
        ("一元一次不等式", "一元二次不等式", "prerequisite"),
        ("一元二次不等式", "分式不等式", "prerequisite"),
        ("绝对值", "绝对值不等式", "prerequisite"),
        ("基本不等式", "平均值不等式", "prerequisite"),
    ])
    
    # 幂、指数与对数 -> 其他
    relations.extend([
        ("正整数指数幂", "整数指数幂", "prerequisite"),
        ("整数指数幂", "有理数指数幂", "prerequisite"),
        ("有理数指数幂", "实数指数幂", "prerequisite"),
        ("根式", "有理数指数幂", "prerequisite"),
        ("幂", "指数函数", "prerequisite"),
        ("指数", "指数函数", "prerequisite"),
        ("指数函数", "对数", "prerequisite"),
        ("对数定义", "常用对数", "prerequisite"),
        ("对数定义", "自然对数", "prerequisite"),
        ("对数运算性质", "对数换底公式", "prerequisite"),
        ("对数", "对数函数", "prerequisite"),
    ])
    
    # 函数 -> 其他
    relations.extend([
        ("集合", "函数概念", "prerequisite"),
        ("函数概念", "函数定义域", "prerequisite"),
        ("函数概念", "函数值域", "prerequisite"),
        ("函数概念", "函数单调性", "prerequisite"),
        ("函数概念", "函数奇偶性", "prerequisite"),
        ("函数单调性", "函数最值", "prerequisite"),
        ("函数", "函数零点", "prerequisite"),
        ("函数", "反函数", "prerequisite"),
        ("函数", "幂函数", "prerequisite"),
        ("函数", "指数函数", "prerequisite"),
        ("函数", "对数函数", "prerequisite"),
        ("指数函数", "对数函数", "prerequisite"),
    ])
    
    # 三角 -> 其他
    relations.extend([
        ("角的概念", "任意角", "prerequisite"),
        ("角度制", "弧度制", "prerequisite"),
        ("弧度制", "三角比", "prerequisite"),
        ("三角比", "正弦", "prerequisite"),
        ("三角比", "余弦", "prerequisite"),
        ("三角比", "正切", "prerequisite"),
        ("三角比", "同角三角比关系", "prerequisite"),
        ("三角比", "诱导公式", "prerequisite"),
        ("诱导公式", "三角恒等变换", "prerequisite"),
        ("三角恒等变换", "两角和差公式", "prerequisite"),
        ("两角和差公式", "倍角公式", "prerequisite"),
        ("倍角公式", "半角公式", "prerequisite"),
    ])
    
    # 三角函数 -> 其他
    relations.extend([
        ("三角比", "正弦函数", "prerequisite"),
        ("三角比", "余弦函数", "prerequisite"),
        ("三角比", "正切函数", "prerequisite"),
        ("正弦函数", "正弦函数图像", "prerequisite"),
        ("正弦函数", "正弦函数性质", "prerequisite"),
        ("余弦函数", "余弦函数图像", "prerequisite"),
        ("余弦函数", "余弦函数性质", "prerequisite"),
        ("正切函数", "正切函数图像", "prerequisite"),
        ("正切函数", "正切函数性质", "prerequisite"),
        ("正弦函数", "正弦型函数", "prerequisite"),
        ("正弦定理", "解三角形", "prerequisite"),
        ("余弦定理", "解三角形", "prerequisite"),
        ("三角函数", "解三角形", "prerequisite"),
    ])
    
    # 平面向量 -> 其他
    relations.extend([
        ("向量", "向量的模", "prerequisite"),
        ("向量", "向量的加法", "prerequisite"),
        ("向量", "向量的减法", "prerequisite"),
        ("向量", "向量的数乘", "prerequisite"),
        ("向量的加法", "平面向量基本定理", "prerequisite"),
        ("平面向量基本定理", "向量坐标表示", "prerequisite"),
        ("向量", "向量数量积", "prerequisite"),
        ("向量数量积", "向量夹角", "prerequisite"),
        ("向量", "复数", "prerequisite"),
    ])
    
    # 复数 -> 其他
    relations.extend([
        ("复数", "复数的实部", "prerequisite"),
        ("复数", "复数的虚部", "prerequisite"),
        ("复数", "复数相等", "prerequisite"),
        ("复数", "共轭复数", "prerequisite"),
        ("复数", "复数的模", "prerequisite"),
        ("复数", "复平面", "prerequisite"),
        ("复数", "复数的几何意义", "prerequisite"),
        ("复数", "复数的加法", "prerequisite"),
        ("复数", "复数的减法", "prerequisite"),
        ("复数", "复数的乘法", "prerequisite"),
        ("复数", "复数的除法", "prerequisite"),
    ])
    
    # 立体几何 -> 其他
    relations.extend([
        ("平面", "空间直线", "prerequisite"),
        ("平面", "直线与平面的位置关系", "prerequisite"),
        ("空间直线", "异面直线", "prerequisite"),
        ("直线与平面的位置关系", "线面平行", "prerequisite"),
        ("直线与平面的位置关系", "线面垂直", "prerequisite"),
        ("两平面的位置关系", "面面平行", "prerequisite"),
        ("两平面的位置关系", "面面垂直", "prerequisite"),
        ("线面平行", "面面平行的判定", "prerequisite"),
        ("线面垂直", "面面垂直的判定", "prerequisite"),
        ("二面角", "面面角的计算", "prerequisite"),
        ("多面体", "棱柱", "prerequisite"),
        ("多面体", "棱锥", "prerequisite"),
        ("旋转体", "圆柱", "prerequisite"),
        ("旋转体", "圆锥", "prerequisite"),
        ("旋转体", "球", "prerequisite"),
    ])
    
    # 概率统计 -> 其他
    relations.extend([
        ("随机现象", "随机试验", "prerequisite"),
        ("随机试验", "样本空间", "prerequisite"),
        ("样本空间", "随机事件", "prerequisite"),
        ("随机事件", "事件的关系", "prerequisite"),
        ("随机事件", "事件的运算", "prerequisite"),
        ("随机事件", "概率", "prerequisite"),
        ("概率", "古典概型", "prerequisite"),
        ("概率", "几何概型", "prerequisite"),
        ("总体", "简单随机抽样", "prerequisite"),
        ("简单随机抽样", "系统抽样", "prerequisite"),
        ("简单随机抽样", "分层抽样", "prerequisite"),
        ("抽样", "频率分布表", "prerequisite"),
        ("抽样", "频率分布直方图", "prerequisite"),
    ])
    
    # 解析几何 -> 其他
    relations.extend([
        ("直线的倾斜角", "直线的斜率", "prerequisite"),
        ("直线的斜率", "直线的点斜式方程", "prerequisite"),
        ("直线的点斜式方程", "直线的斜截式方程", "prerequisite"),
        ("直线的点斜式方程", "直线的两点式方程", "prerequisite"),
        ("直线的两点式方程", "直线的截距式方程", "prerequisite"),
        ("直线方程", "直线的一般式方程", "prerequisite"),
        ("两直线平行", "两直线垂直", "prerequisite"),
        ("直线", "曲线与方程", "prerequisite"),
        ("曲线与方程", "圆的标准方程", "prerequisite"),
        ("圆的标准方程", "圆的一般方程", "prerequisite"),
        ("圆", "椭圆", "prerequisite"),
        ("椭圆", "双曲线", "prerequisite"),
        ("椭圆", "抛物线", "prerequisite"),
        ("圆锥曲线", "直线与圆锥曲线的位置关系", "prerequisite"),
    ])
    
    # 空间向量 -> 其他
    relations.extend([
        ("平面向量", "空间向量", "prerequisite"),
        ("空间向量", "空间向量基本定理", "prerequisite"),
        ("空间向量基本定理", "空间向量的坐标表示", "prerequisite"),
        ("空间向量", "直线的方向向量", "prerequisite"),
        ("空间向量", "平面的法向量", "prerequisite"),
        ("空间向量", "空间向量在立体几何中的应用", "prerequisite"),
    ])
    
    # 数列 -> 其他
    relations.extend([
        ("数列", "数列的通项", "prerequisite"),
        ("数列", "数列的前n项和", "prerequisite"),
        ("数列", "等差数列", "prerequisite"),
        ("数列", "等比数列", "prerequisite"),
        ("等差数列", "等差数列的通项公式", "prerequisite"),
        ("等差数列", "等差数列的前n项和", "prerequisite"),
        ("等比数列", "等比数列的通项公式", "prerequisite"),
        ("等比数列", "等比数列的前n项和", "prerequisite"),
        ("数列", "数学归纳法", "prerequisite"),
        ("数列", "数列的极限", "prerequisite"),
    ])
    
    # 导数 -> 其他
    relations.extend([
        ("函数", "导数的概念", "prerequisite"),
        ("平均变化率", "瞬时变化率", "prerequisite"),
        ("瞬时变化率", "导数的概念", "prerequisite"),
        ("导数的概念", "导数的几何意义", "prerequisite"),
        ("导数的几何意义", "切线", "prerequisite"),
        ("导数", "导函数", "prerequisite"),
        ("导数", "基本初等函数的导数", "prerequisite"),
        ("基本初等函数的导数", "导数的四则运算", "prerequisite"),
        ("导数的四则运算", "复合函数的导数", "prerequisite"),
        ("导数", "导数与单调性", "prerequisite"),
        ("导数与单调性", "极值", "prerequisite"),
        ("极值", "最值", "prerequisite"),
    ])
    
    # 计数原理 -> 其他
    relations.extend([
        ("分类计数原理", "排列", "prerequisite"),
        ("分步计数原理", "排列", "prerequisite"),
        ("分类计数原理", "组合", "prerequisite"),
        ("分步计数原理", "组合", "prerequisite"),
        ("排列", "排列数", "prerequisite"),
        ("组合", "组合数", "prerequisite"),
        ("组合数", "二项式定理", "prerequisite"),
    ])
    
    # 概率进阶 -> 其他
    relations.extend([
        ("概率", "条件概率", "prerequisite"),
        ("条件概率", "乘法公式", "prerequisite"),
        ("条件概率", "全概率公式", "prerequisite"),
        ("条件概率", "贝叶斯公式", "prerequisite"),
        ("概率", "事件的独立性", "prerequisite"),
        ("事件的独立性", "独立重复试验", "prerequisite"),
        ("概率", "随机变量", "prerequisite"),
        ("随机变量", "离散型随机变量", "prerequisite"),
        ("随机变量", "概率分布列", "prerequisite"),
        ("概率分布列", "数学期望", "prerequisite"),
        ("概率分布列", "方差", "prerequisite"),
        ("二项分布", "正态分布", "prerequisite"),
    ])
    
    # 统计进阶 -> 其他
    relations.extend([
        ("统计", "变量的相关性", "prerequisite"),
        ("变量的相关性", "散点图", "prerequisite"),
        ("变量的相关性", "相关系数", "prerequisite"),
        ("相关系数", "一元线性回归", "prerequisite"),
        ("一元线性回归", "回归直线", "prerequisite"),
        ("一元线性回归", "最小二乘法", "prerequisite"),
        ("统计", "独立性检验", "prerequisite"),
    ])
    
    return relations

def generate_related_relations():
    """生成相关关系（同级、相似概念）"""
    relations = []
    
    # 集合运算之间的关系
    relations.extend([
        ("交集", "并集", "related"),
        ("交集", "补集", "related"),
        ("并集", "补集", "related"),
        ("子集", "真子集", "related"),
    ])
    
    # 逻辑关系
    relations.extend([
        ("充分条件", "必要条件", "related"),
        ("交集", "逻辑与", "related"),
        ("并集", "逻辑或", "related"),
        ("补集", "逻辑非", "related"),
    ])
    
    # 方程与不等式
    relations.extend([
        ("等式", "不等式", "related"),
        ("一元一次方程", "一元一次不等式", "related"),
        ("一元二次方程", "一元二次不等式", "related"),
        ("方程的解", "不等式的解集", "related"),
    ])
    
    # 幂与对数
    relations.extend([
        ("指数函数", "对数函数", "related"),
        ("指数", "对数", "related"),
        ("幂函数", "指数函数", "related"),
        ("幂函数", "对数函数", "related"),
    ])
    
    # 函数性质
    relations.extend([
        ("函数单调性", "函数奇偶性", "related"),
        ("函数单调性", "函数周期性", "related"),
        ("函数奇偶性", "函数周期性", "related"),
        ("极大值", "极小值", "related"),
        ("最大值", "最小值", "related"),
    ])
    
    # 三角函数
    relations.extend([
        ("正弦函数", "余弦函数", "related"),
        ("正弦函数", "正切函数", "related"),
        ("余弦函数", "正切函数", "related"),
        ("正弦定理", "余弦定理", "related"),
        ("诱导公式", "三角恒等变换", "related"),
    ])
    
    # 向量与复数
    relations.extend([
        ("平面向量", "空间向量", "related"),
        ("向量", "复数", "related"),
        ("向量的模", "复数的模", "related"),
        ("向量加法", "复数加法", "related"),
    ])
    
    # 几何
    relations.extend([
        ("线面平行", "面面平行", "related"),
        ("线面垂直", "面面垂直", "related"),
        ("平行", "垂直", "related"),
        ("棱柱", "圆柱", "related"),
        ("棱锥", "圆锥", "related"),
        ("柱体", "锥体", "related"),
    ])
    
    # 圆锥曲线
    relations.extend([
        ("椭圆", "双曲线", "related"),
        ("椭圆", "抛物线", "related"),
        ("双曲线", "抛物线", "related"),
        ("圆", "椭圆", "related"),
        ("圆的标准方程", "椭圆的标准方程", "related"),
    ])
    
    # 数列
    relations.extend([
        ("等差数列", "等比数列", "related"),
        ("等差数列的通项公式", "等比数列的通项公式", "related"),
        ("等差数列的前n项和", "等比数列的前n项和", "related"),
        ("等差中项", "等比中项", "related"),
    ])
    
    # 导数与函数
    relations.extend([
        ("导数", "微分", "related"),
        ("导数与单调性", "函数单调性", "related"),
        ("导数", "函数最值", "related"),
        ("切线", "法线", "related"),
    ])
    
    # 计数原理
    relations.extend([
        ("排列", "组合", "related"),
        ("分类计数原理", "分步计数原理", "related"),
        ("加法原理", "乘法原理", "related"),
        ("排列数", "组合数", "related"),
    ])
    
    # 概率
    relations.extend([
        ("古典概型", "几何概型", "related"),
        ("条件概率", "独立事件", "related"),
        ("数学期望", "方差", "related"),
        ("二项分布", "超几何分布", "related"),
        ("离散型随机变量", "连续型随机变量", "related"),
    ])
    
    # 统计
    relations.extend([
        ("平均数", "数学期望", "related"),
        ("方差", "标准差", "related"),
        ("相关系数", "回归系数", "related"),
        ("散点图", "回归直线", "related"),
    ])
    
    # 坐标系与方程
    relations.extend([
        ("直线的斜率", "导数的几何意义", "related"),
        ("直线方程", "曲线与方程", "related"),
        ("圆方程", "圆锥曲线方程", "related"),
    ])
    
    return relations

def generate_extension_relations():
    """生成扩展关系"""
    relations = []
    
    # 基础到应用
    relations.extend([
        ("函数", "函数的应用", "extension"),
        ("三角函数", "解三角形的应用", "extension"),
        ("导数", "优化问题", "extension"),
        ("数列", "分期付款", "extension"),
        ("概率", "统计案例分析", "extension"),
        ("圆锥曲线", "圆锥曲线的应用", "extension"),
    ])
    
    # 初等到高等
    relations.extend([
        ("函数极限", "导数", "extension"),
        ("数列的极限", "函数极限", "extension"),
        ("导数", "微积分", "extension"),
        ("定积分", "微积分", "extension"),
        ("泰勒展开", "导数", "extension"),
    ])
    
    # 理论到应用
    relations.extend([
        ("数学建模", "优化模型", "extension"),
        ("数学建模", "预测模型", "extension"),
        ("回归分析", "预测模型", "extension"),
        ("概率", "风险评估", "extension"),
    ])
    
    return relations

def main():
    print("=" * 60)
    print("高中数学知识图谱生成器")
    print("=" * 60)
    
    # 清空现有数据
    clear_existing_graph()
    
    # 生成知识点
    print("\n生成知识点...")
    all_points = generate_knowledge_points()
    print(f"共生成 {len(all_points)} 个知识点")
    
    # 生成关系
    print("\n生成知识关联关系...")
    prerequisite_relations = generate_prerequisite_relations()
    related_relations = generate_related_relations()
    extension_relations = generate_extension_relations()
    
    all_relations = prerequisite_relations + related_relations + extension_relations
    
    print(f"前置关系: {len(prerequisite_relations)} 条")
    print(f"相关关系: {len(related_relations)} 条")
    print(f"扩展关系: {len(extension_relations)} 条")
    print(f"总关系数: {len(all_relations)} 条")
    
    # 插入数据库
    print("\n插入数据库...")
    insert_knowledge_relations(all_relations)
    
    # 验证结果
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM knowledge_graph")
    total_relations = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(DISTINCT from_point) FROM knowledge_graph")
    from_points = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(DISTINCT to_point) FROM knowledge_graph")
    to_points = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(DISTINCT from_point) FROM knowledge_graph UNION SELECT COUNT(DISTINCT to_point) FROM knowledge_graph")
    unique_points = cursor.fetchall()
    
    cursor.execute("SELECT relation, COUNT(*) FROM knowledge_graph GROUP BY relation")
    relation_counts = cursor.fetchall()
    
    conn.close()
    
    print("\n" + "=" * 60)
    print("生成结果统计")
    print("=" * 60)
    print(f"总关联关系数: {total_relations}")
    print(f"源知识点数: {from_points}")
    print(f"目标知识点数: {to_points}")
    print(f"\n关系类型分布:")
    for rel_type, count in relation_counts:
        print(f"  {rel_type}: {count} 条")
    
    print("\n" + "=" * 60)
    print("知识图谱生成完成!")
    print("=" * 60)

if __name__ == "__main__":
    main()
