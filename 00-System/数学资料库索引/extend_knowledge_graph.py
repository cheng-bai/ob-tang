#!/usr/bin/env python3
"""
扩展高中数学知识图谱数据
添加更多知识点和关联关系，达到500+关系
"""

import sqlite3

# 数据库路径
DB_PATH = '/Users/tangchengbaiair/Downloads/mini-数学资料库/00-索引与配置/teaching_index.db'

def get_existing_relations():
    """获取现有关系数量"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM knowledge_graph")
    count = cursor.fetchone()[0]
    conn.close()
    return count

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

def generate_additional_prerequisites():
    """生成更多前置关系"""
    relations = []
    
    # 更详细的集合关系
    relations.extend([
        ("集合", "空集", "prerequisite"),
        ("集合", "有限集", "prerequisite"),
        ("集合", "无限集", "prerequisite"),
        ("集合", "子集", "prerequisite"),
        ("子集", "真子集", "prerequisite"),
        ("子集", "集合相等", "prerequisite"),
        ("集合的表示法", "列举法", "prerequisite"),
        ("集合的表示法", "描述法", "prerequisite"),
        ("描述法", "区间表示", "prerequisite"),
        ("交集", "德摩根定律", "prerequisite"),
        ("并集", "德摩根定律", "prerequisite"),
        ("补集", "德摩根定律", "prerequisite"),
    ])
    
    # 更详细的方程关系
    relations.extend([
        ("一元二次方程", "因式分解法", "prerequisite"),
        ("一元二次方程", "配方法", "prerequisite"),
        ("一元二次方程", "公式法", "prerequisite"),
        ("判别式", "根的情况判断", "prerequisite"),
        ("韦达定理", "构造方程", "prerequisite"),
        ("韦达定理", "根与系数的关系", "prerequisite"),
        ("一元二次不等式", "二次函数图像", "prerequisite"),
        ("一元二次不等式", "穿根法", "prerequisite"),
        ("分式不等式", "分式方程", "prerequisite"),
        ("绝对值不等式", "绝对值的几何意义", "prerequisite"),
        ("基本不等式", "均值不等式链", "prerequisite"),
        ("基本不等式", "一正二定三相等", "prerequisite"),
    ])
    
    # 更详细的函数关系
    relations.extend([
        ("函数概念", "映射", "prerequisite"),
        ("函数定义域", "分母不为零", "prerequisite"),
        ("函数定义域", "偶次根式被开方数非负", "prerequisite"),
        ("函数定义域", "对数真数大于零", "prerequisite"),
        ("函数定义域", "零次幂底数不为零", "prerequisite"),
        ("函数值域", "配方法求值域", "prerequisite"),
        ("函数值域", "分离常数法", "prerequisite"),
        ("函数值域", "换元法", "prerequisite"),
        ("函数单调性", "单调性的证明", "prerequisite"),
        ("函数单调性", "复合函数单调性", "prerequisite"),
        ("函数奇偶性", "奇偶性的判断", "prerequisite"),
        ("函数奇偶性", "奇偶函数图像特征", "prerequisite"),
        ("函数周期性", "周期函数的性质", "prerequisite"),
        ("函数零点", "零点存在定理", "prerequisite"),
        ("函数零点", "二分法求零点", "prerequisite"),
        ("反函数", "反函数的求法", "prerequisite"),
        ("反函数", "互为反函数的图像关系", "prerequisite"),
    ])
    
    # 幂指对函数详细关系
    relations.extend([
        ("正整数指数幂", "幂的运算性质", "prerequisite"),
        ("整数指数幂", "科学记数法", "prerequisite"),
        ("有理数指数幂", "根式化简", "prerequisite"),
        ("根式", "根式的运算", "prerequisite"),
        ("根式", "分母有理化", "prerequisite"),
        ("指数函数", "指数函数图像", "prerequisite"),
        ("指数函数", "指数函数性质", "prerequisite"),
        ("指数函数", "指数函数应用", "prerequisite"),
        ("对数", "对数恒等式", "prerequisite"),
        ("对数", "对数方程", "prerequisite"),
        ("对数函数", "对数函数图像", "prerequisite"),
        ("对数函数", "对数函数性质", "prerequisite"),
        ("对数函数", "对数函数应用", "prerequisite"),
        ("幂函数", "幂函数图像", "prerequisite"),
        ("幂函数", "幂函数性质", "prerequisite"),
    ])
    
    # 三角详细关系
    relations.extend([
        ("任意角", "象限角", "prerequisite"),
        ("任意角", "终边相同的角", "prerequisite"),
        ("弧度制", "弧长公式", "prerequisite"),
        ("弧度制", "扇形面积公式", "prerequisite"),
        ("三角比", "单位圆", "prerequisite"),
        ("正弦", "正弦线", "prerequisite"),
        ("余弦", "余弦线", "prerequisite"),
        ("正切", "正切线", "prerequisite"),
        ("同角三角比关系", "平方关系", "prerequisite"),
        ("同角三角比关系", "商数关系", "prerequisite"),
        ("同角三角比关系", "倒数关系", "prerequisite"),
        ("诱导公式", "奇变偶不变", "prerequisite"),
        ("诱导公式", "符号看象限", "prerequisite"),
        ("两角和差公式", "和差化积", "prerequisite"),
        ("两角和差公式", "积化和差", "prerequisite"),
        ("倍角公式", "降幂公式", "prerequisite"),
        ("倍角公式", "升幂公式", "prerequisite"),
    ])
    
    # 三角函数详细关系
    relations.extend([
        ("正弦函数图像", "五点作图法", "prerequisite"),
        ("正弦函数性质", "周期性", "prerequisite"),
        ("正弦函数性质", "单调性", "prerequisite"),
        ("正弦函数性质", "奇偶性", "prerequisite"),
        ("正弦函数性质", "最值", "prerequisite"),
        ("正弦函数性质", "对称性", "prerequisite"),
        ("正弦型函数", "振幅变换", "prerequisite"),
        ("正弦型函数", "周期变换", "prerequisite"),
        ("正弦型函数", "相位变换", "prerequisite"),
        ("正弦型函数", "上下平移", "prerequisite"),
        ("余弦函数", "正弦函数", "prerequisite"),
        ("正切函数", "正切函数定义域", "prerequisite"),
        ("正切函数", "正切函数值域", "prerequisite"),
        ("解三角形", "三角形面积公式", "prerequisite"),
        ("解三角形", "射影定理", "prerequisite"),
        ("解三角形", "实际应用", "prerequisite"),
    ])
    
    # 向量详细关系
    relations.extend([
        ("向量", "有向线段", "prerequisite"),
        ("向量", "自由向量", "prerequisite"),
        ("向量的加法", "平行四边形法则", "prerequisite"),
        ("向量的加法", "三角形法则", "prerequisite"),
        ("向量的减法", "向量的加法", "prerequisite"),
        ("向量的数乘", "共线向量", "prerequisite"),
        ("平面向量基本定理", "基底", "prerequisite"),
        ("向量坐标表示", "向量运算的坐标表示", "prerequisite"),
        ("向量数量积", "向量垂直的判定", "prerequisite"),
        ("向量数量积", "向量模的计算", "prerequisite"),
        ("向量数量积", "向量夹角的计算", "prerequisite"),
        ("向量", "定比分点公式", "prerequisite"),
        ("向量", "重心坐标公式", "prerequisite"),
    ])
    
    # 复数详细关系
    relations.extend([
        ("虚数单位", "复数定义", "prerequisite"),
        ("复数", "纯虚数", "prerequisite"),
        ("复数", "实数", "prerequisite"),
        ("复数相等", "复数运算", "prerequisite"),
        ("共轭复数", "复数模的性质", "prerequisite"),
        ("复平面", "实轴", "prerequisite"),
        ("复平面", "虚轴", "prerequisite"),
        ("复数的几何意义", "复数的向量表示", "prerequisite"),
        ("复数的加法", "平行四边形法则", "prerequisite"),
        ("复数的减法", "三角形法则", "prerequisite"),
        ("复数的乘法", "多项式乘法", "prerequisite"),
        ("复数的除法", "分母实数化", "prerequisite"),
        ("复数的三角形式", "复数的乘法", "prerequisite"),
        ("复数的三角形式", "复数的除法", "prerequisite"),
        ("棣莫弗定理", "复数的乘方", "prerequisite"),
    ])
    
    # 立体几何详细关系
    relations.extend([
        ("平面", "平面的基本性质", "prerequisite"),
        ("平面", "确定平面的条件", "prerequisite"),
        ("空间直线", "异面直线的判定", "prerequisite"),
        ("空间直线", "异面直线所成的角", "prerequisite"),
        ("空间直线", "异面直线的距离", "prerequisite"),
        ("线面平行", "线面平行的判定定理", "prerequisite"),
        ("线面平行", "线面平行的性质定理", "prerequisite"),
        ("面面平行", "面面平行的判定定理", "prerequisite"),
        ("面面平行", "面面平行的性质定理", "prerequisite"),
        ("线面垂直", "线面垂直的判定定理", "prerequisite"),
        ("线面垂直", "线面垂直的性质定理", "prerequisite"),
        ("线面垂直", "点到平面的距离", "prerequisite"),
        ("面面垂直", "面面垂直的判定定理", "prerequisite"),
        ("面面垂直", "面面垂直的性质定理", "prerequisite"),
        ("二面角", "二面角的平面角", "prerequisite"),
        ("三垂线定理", "线面垂直", "prerequisite"),
    ])
    
    # 几何体详细关系
    relations.extend([
        ("棱柱", "直棱柱", "prerequisite"),
        ("棱柱", "斜棱柱", "prerequisite"),
        ("棱柱", "正棱柱", "prerequisite"),
        ("棱锥", "正棱锥", "prerequisite"),
        ("圆柱", "圆柱的轴截面", "prerequisite"),
        ("圆锥", "圆锥的轴截面", "prerequisite"),
        ("球", "球的大圆", "prerequisite"),
        ("球", "球的小圆", "prerequisite"),
        ("球", "球面距离", "prerequisite"),
        ("柱体", "柱体的体积公式", "prerequisite"),
        ("柱体", "柱体的表面积", "prerequisite"),
        ("锥体", "锥体的体积公式", "prerequisite"),
        ("锥体", "锥体的表面积", "prerequisite"),
        ("台体", "台体的体积公式", "prerequisite"),
        ("球", "球的表面积公式", "prerequisite"),
        ("球", "球的体积公式", "prerequisite"),
        ("直观图", "斜二测画法", "prerequisite"),
        ("三视图", "正视图", "prerequisite"),
        ("三视图", "侧视图", "prerequisite"),
        ("三视图", "俯视图", "prerequisite"),
    ])
    
    # 概率统计详细关系
    relations.extend([
        ("随机试验", "样本点", "prerequisite"),
        ("样本点", "样本空间", "prerequisite"),
        ("随机事件", "基本事件", "prerequisite"),
        ("随机事件", "复合事件", "prerequisite"),
        ("事件的关系", "包含关系", "prerequisite"),
        ("事件的关系", "相等关系", "prerequisite"),
        ("互斥事件", "对立事件", "prerequisite"),
        ("事件的运算", "并事件", "prerequisite"),
        ("事件的运算", "交事件", "prerequisite"),
        ("事件的运算", "对立事件", "prerequisite"),
        ("概率", "频率", "prerequisite"),
        ("古典概型", "等可能性", "prerequisite"),
        ("古典概型", "有限性", "prerequisite"),
        ("几何概型", "无限性", "prerequisite"),
        ("几何概型", "等可能性", "prerequisite"),
        ("抽样", "总体", "prerequisite"),
        ("抽样", "个体", "prerequisite"),
        ("抽样", "样本", "prerequisite"),
        ("简单随机抽样", "抽签法", "prerequisite"),
        ("简单随机抽样", "随机数表法", "prerequisite"),
        ("分层抽样", "按比例分配", "prerequisite"),
        ("频率分布表", "组距", "prerequisite"),
        ("频率分布表", "频数", "prerequisite"),
        ("频率分布直方图", "频率分布表", "prerequisite"),
        ("平均数", "加权平均数", "prerequisite"),
        ("方差", "标准差", "prerequisite"),
    ])
    
    # 解析几何详细关系
    relations.extend([
        ("直线的倾斜角", "倾斜角的范围", "prerequisite"),
        ("直线的斜率", "斜率与倾斜角的关系", "prerequisite"),
        ("直线的斜率", "过两点的斜率公式", "prerequisite"),
        ("点斜式方程", "斜截式方程", "prerequisite"),
        ("两点式方程", "截距式方程", "prerequisite"),
        ("截距式方程", "直线的一般式方程", "prerequisite"),
        ("两直线平行", "斜率相等", "prerequisite"),
        ("两直线垂直", "斜率乘积为-1", "prerequisite"),
        ("点到直线的距离", "距离公式", "prerequisite"),
        ("两平行线间的距离", "距离公式", "prerequisite"),
        ("曲线与方程", "求曲线方程的步骤", "prerequisite"),
        ("圆的标准方程", "圆心和半径", "prerequisite"),
        ("圆的一般方程", "配方化为标准方程", "prerequisite"),
        ("点与圆的位置关系", "点到圆心距离", "prerequisite"),
        ("直线与圆的位置关系", "判别式法", "prerequisite"),
        ("直线与圆的位置关系", "几何法", "prerequisite"),
        ("圆与圆的位置关系", "圆心距与半径", "prerequisite"),
        ("椭圆", "椭圆的定义", "prerequisite"),
        ("椭圆", "椭圆的标准方程", "prerequisite"),
        ("椭圆", "椭圆的几何性质", "prerequisite"),
        ("椭圆", "椭圆的离心率", "prerequisite"),
        ("双曲线", "双曲线的定义", "prerequisite"),
        ("双曲线", "双曲线的标准方程", "prerequisite"),
        ("双曲线", "双曲线的几何性质", "prerequisite"),
        ("双曲线", "双曲线的渐近线", "prerequisite"),
        ("抛物线", "抛物线的定义", "prerequisite"),
        ("抛物线", "抛物线的标准方程", "prerequisite"),
        ("抛物线", "抛物线的几何性质", "prerequisite"),
        ("直线与圆锥曲线", "联立方程", "prerequisite"),
        ("直线与圆锥曲线", "弦长公式", "prerequisite"),
        ("直线与圆锥曲线", "韦达定理的应用", "prerequisite"),
    ])
    
    # 空间向量详细关系
    relations.extend([
        ("空间向量", "空间向量的模", "prerequisite"),
        ("空间向量", "空间向量的相等", "prerequisite"),
        ("空间向量的加法", "空间向量的三角形法则", "prerequisite"),
        ("空间向量的加法", "空间向量的平行四边形法则", "prerequisite"),
        ("空间向量的数乘", "共线向量定理", "prerequisite"),
        ("空间向量基本定理", "基底", "prerequisite"),
        ("空间向量基本定理", "基向量", "prerequisite"),
        ("空间向量的坐标表示", "空间向量运算的坐标表示", "prerequisite"),
        ("空间向量的数量积", "空间向量垂直的判定", "prerequisite"),
        ("空间向量的数量积", "空间向量模的计算", "prerequisite"),
        ("空间向量的数量积", "空间向量夹角的计算", "prerequisite"),
        ("直线的方向向量", "直线的向量方程", "prerequisite"),
        ("平面的法向量", "平面方程", "prerequisite"),
        ("空间向量", "异面直线所成的角", "prerequisite"),
        ("空间向量", "线面角", "prerequisite"),
        ("空间向量", "二面角", "prerequisite"),
        ("空间向量", "点到平面的距离", "prerequisite"),
    ])
    
    # 数列详细关系
    relations.extend([
        ("数列", "数列的分类", "prerequisite"),
        ("数列", "有穷数列", "prerequisite"),
        ("数列", "无穷数列", "prerequisite"),
        ("数列", "递增数列", "prerequisite"),
        ("数列", "递减数列", "prerequisite"),
        ("数列", "常数列", "prerequisite"),
        ("数列", "摆动数列", "prerequisite"),
        ("数列的通项", "通项公式的求法", "prerequisite"),
        ("数列的前n项和", "Sn与an的关系", "prerequisite"),
        ("等差数列", "等差数列的定义", "prerequisite"),
        ("等差数列", "等差数列的通项公式", "prerequisite"),
        ("等差数列", "等差数列的性质", "prerequisite"),
        ("等差数列", "等差中项", "prerequisite"),
        ("等差数列的前n项和", "倒序相加法", "prerequisite"),
        ("等差数列的前n项和", "等差数列和的最值", "prerequisite"),
        ("等比数列", "等比数列的定义", "prerequisite"),
        ("等比数列", "等比数列的通项公式", "prerequisite"),
        ("等比数列", "等比数列的性质", "prerequisite"),
        ("等比数列", "等比中项", "prerequisite"),
        ("等比数列的前n项和", "错位相减法", "prerequisite"),
        ("数列求和", "公式法", "prerequisite"),
        ("数列求和", "分组求和法", "prerequisite"),
        ("数列求和", "裂项相消法", "prerequisite"),
        ("数列求和", "错位相减法", "prerequisite"),
        ("数列求和", "倒序相加法", "prerequisite"),
        ("数学归纳法", "归纳奠基", "prerequisite"),
        ("数学归纳法", "归纳递推", "prerequisite"),
        ("数列的极限", "极限的四则运算", "prerequisite"),
        ("数列的极限", "无穷等比数列的和", "prerequisite"),
    ])
    
    # 导数详细关系
    relations.extend([
        ("平均变化率", "函数的变化率", "prerequisite"),
        ("瞬时变化率", "导数的定义", "prerequisite"),
        ("导数的概念", "可导与连续", "prerequisite"),
        ("导数的几何意义", "切线斜率", "prerequisite"),
        ("导数的几何意义", "瞬时速度", "prerequisite"),
        ("基本初等函数的导数", "常数的导数", "prerequisite"),
        ("基本初等函数的导数", "幂函数的导数", "prerequisite"),
        ("基本初等函数的导数", "指数函数的导数", "prerequisite"),
        ("基本初等函数的导数", "对数函数的导数", "prerequisite"),
        ("基本初等函数的导数", "三角函数的导数", "prerequisite"),
        ("导数的四则运算", "和差的导数", "prerequisite"),
        ("导数的四则运算", "积的导数", "prerequisite"),
        ("导数的四则运算", "商的导数", "prerequisite"),
        ("复合函数的导数", "链式法则", "prerequisite"),
        ("导数与单调性", "求单调区间", "prerequisite"),
        ("极值", "极值点的判定", "prerequisite"),
        ("极值", "求极值的方法", "prerequisite"),
        ("最值", "闭区间上最值的求法", "prerequisite"),
        ("最值", "开区间上最值的求法", "prerequisite"),
        ("导数的应用", "证明不等式", "prerequisite"),
        ("导数的应用", "讨论方程根的情况", "prerequisite"),
        ("导数的应用", "实际应用问题", "prerequisite"),
    ])
    
    # 计数原理详细关系
    relations.extend([
        ("分类计数原理", "分类加法", "prerequisite"),
        ("分步计数原理", "分步乘法", "prerequisite"),
        ("排列", "排列的定义", "prerequisite"),
        ("排列", "排列数公式", "prerequisite"),
        ("排列", "全排列", "prerequisite"),
        ("排列", "阶乘", "prerequisite"),
        ("组合", "组合的定义", "prerequisite"),
        ("组合", "组合数公式", "prerequisite"),
        ("组合数", "组合数的性质", "prerequisite"),
        ("组合数", "杨辉三角", "prerequisite"),
        ("排列组合", "特殊元素优先法", "prerequisite"),
        ("排列组合", "捆绑法", "prerequisite"),
        ("排列组合", "插空法", "prerequisite"),
        ("排列组合", "隔板法", "prerequisite"),
        ("排列组合", "排除法", "prerequisite"),
        ("二项式定理", "二项展开式", "prerequisite"),
        ("二项式定理", "通项公式", "prerequisite"),
        ("二项式系数", "二项式系数的性质", "prerequisite"),
        ("二项式系数", "赋值法", "prerequisite"),
    ])
    
    # 概率进阶详细关系
    relations.extend([
        ("条件概率", "条件概率的定义", "prerequisite"),
        ("条件概率", "条件概率公式", "prerequisite"),
        ("乘法公式", "条件概率", "prerequisite"),
        ("全概率公式", "完备事件组", "prerequisite"),
        ("贝叶斯公式", "条件概率", "prerequisite"),
        ("贝叶斯公式", "全概率公式", "prerequisite"),
        ("事件的独立性", "独立性的判定", "prerequisite"),
        ("独立重复试验", "n次独立重复试验", "prerequisite"),
        ("随机变量", "离散型随机变量", "prerequisite"),
        ("随机变量", "连续型随机变量", "prerequisite"),
        ("概率分布列", "分布列的性质", "prerequisite"),
        ("两点分布", "二项分布", "prerequisite"),
        ("二项分布", "二项分布的期望", "prerequisite"),
        ("二项分布", "二项分布的方差", "prerequisite"),
        ("超几何分布", "超几何分布的期望", "prerequisite"),
        ("超几何分布", "超几何分布的方差", "prerequisite"),
        ("数学期望", "期望的性质", "prerequisite"),
        ("方差", "方差的性质", "prerequisite"),
        ("方差", "标准差", "prerequisite"),
        ("正态分布", "正态曲线", "prerequisite"),
        ("正态分布", "正态分布的性质", "prerequisite"),
        ("正态分布", "标准正态分布", "prerequisite"),
        ("正态分布", "3σ原则", "prerequisite"),
    ])
    
    # 统计进阶详细关系
    relations.extend([
        ("变量的相关性", "正相关", "prerequisite"),
        ("变量的相关性", "负相关", "prerequisite"),
        ("变量的相关性", "线性相关", "prerequisite"),
        ("散点图", "相关关系", "prerequisite"),
        ("相关系数", "相关系数的计算", "prerequisite"),
        ("相关系数", "相关系数的意义", "prerequisite"),
        ("一元线性回归", "回归分析", "prerequisite"),
        ("回归直线", "最小二乘法", "prerequisite"),
        ("回归方程", "回归系数", "prerequisite"),
        ("回归方程", "相关指数", "prerequisite"),
        ("独立性检验", "2×2列联表", "prerequisite"),
        ("独立性检验", "卡方统计量", "prerequisite"),
        ("独立性检验", "独立性检验的步骤", "prerequisite"),
    ])
    
    return relations

def generate_additional_related():
    """生成更多相关关系"""
    relations = []
    
    # 函数相关
    relations.extend([
        ("一次函数", "直线方程", "related"),
        ("二次函数", "抛物线", "related"),
        ("反比例函数", "双曲线", "related"),
        ("指数函数", "对数函数", "related"),
        ("幂函数", "指数函数", "related"),
        ("三角函数", "反三角函数", "related"),
    ])
    
    # 几何相关
    relations.extend([
        ("平面几何", "立体几何", "related"),
        ("解析几何", "向量几何", "related"),
        ("欧氏几何", "非欧几何", "related"),
        ("正弦定理", "余弦定理", "related"),
        ("勾股定理", "余弦定理", "related"),
    ])
    
    # 代数相关
    relations.extend([
        ("代数", "几何", "related"),
        ("代数运算", "几何直观", "related"),
        ("方程", "不等式", "related"),
        ("等式", "恒等式", "related"),
    ])
    
    # 数列与函数
    relations.extend([
        ("等差数列", "一次函数", "related"),
        ("等比数列", "指数函数", "related"),
        ("数列求和", "定积分", "related"),
    ])
    
    # 微积分相关
    relations.extend([
        ("导数", "微分", "related"),
        ("定积分", "不定积分", "related"),
        ("微分", "积分", "related"),
        ("导数", "变化率", "related"),
        ("积分", "面积", "related"),
    ])
    
    # 概率统计相关
    relations.extend([
        ("概率论", "数理统计", "related"),
        ("频率", "概率", "related"),
        ("样本", "总体", "related"),
        ("参数估计", "假设检验", "related"),
    ])
    
    # 向量与复数
    relations.extend([
        ("向量", "复数", "related"),
        ("平面向量", "空间向量", "related"),
        ("向量运算", "复数运算", "related"),
    ])
    
    # 坐标系
    relations.extend([
        ("直角坐标系", "极坐标系", "related"),
        ("直角坐标系", "参数方程", "related"),
        ("平面坐标系", "空间坐标系", "related"),
    ])
    
    # 圆锥曲线相关
    relations.extend([
        ("椭圆", "圆", "related"),
        ("双曲线", "椭圆", "related"),
        ("抛物线", "椭圆", "related"),
        ("抛物线", "二次函数", "related"),
    ])
    
    # 三角相关
    relations.extend([
        ("正弦", "余弦", "related"),
        ("正切", "余切", "related"),
        ("正割", "余割", "related"),
        ("弧度制", "角度制", "related"),
    ])
    
    # 数论相关
    relations.extend([
        ("质数", "合数", "related"),
        ("奇数", "偶数", "related"),
        ("整数", "有理数", "related"),
        ("有理数", "无理数", "related"),
        ("实数", "复数", "related"),
    ])
    
    # 集合论相关
    relations.extend([
        ("交集", "并集", "related"),
        ("子集", "真子集", "related"),
        ("有限集", "无限集", "related"),
        ("可数集", "不可数集", "related"),
    ])
    
    # 逻辑相关
    relations.extend([
        ("充分条件", "必要条件", "related"),
        ("充分不必要", "必要不充分", "related"),
        ("命题", "逆命题", "related"),
        ("命题", "否命题", "related"),
        ("命题", "逆否命题", "related"),
    ])
    
    # 运算相关
    relations.extend([
        ("加法", "减法", "related"),
        ("乘法", "除法", "related"),
        ("乘方", "开方", "related"),
        ("指数运算", "对数运算", "related"),
    ])
    
    # 方程相关
    relations.extend([
        ("一元一次方程", "二元一次方程", "related"),
        ("一元二次方程", "高次方程", "related"),
        ("整式方程", "分式方程", "related"),
        ("代数方程", "超越方程", "related"),
    ])
    
    # 不等式相关
    relations.extend([
        ("一元一次不等式", "一元二次不等式", "related"),
        ("整式不等式", "分式不等式", "related"),
        ("绝对值不等式", "无理不等式", "related"),
    ])
    
    # 几何体相关
    relations.extend([
        ("柱体", "锥体", "related"),
        ("棱柱", "圆柱", "related"),
        ("棱锥", "圆锥", "related"),
        ("棱台", "圆台", "related"),
    ])
    
    # 抽样方法相关
    relations.extend([
        ("简单随机抽样", "系统抽样", "related"),
        ("简单随机抽样", "分层抽样", "related"),
        ("系统抽样", "分层抽样", "related"),
    ])
    
    # 统计量相关
    relations.extend([
        ("平均数", "中位数", "related"),
        ("平均数", "众数", "related"),
        ("方差", "标准差", "related"),
        ("极差", "四分位距", "related"),
    ])
    
    # 概率分布相关
    relations.extend([
        ("两点分布", "二项分布", "related"),
        ("二项分布", "正态分布", "related"),
        ("超几何分布", "二项分布", "related"),
        ("泊松分布", "二项分布", "related"),
    ])
    
    # 回归分析相关
    relations.extend([
        ("线性回归", "非线性回归", "related"),
        ("一元回归", "多元回归", "related"),
        ("相关分析", "回归分析", "related"),
    ])
    
    # 数学思想方法
    relations.extend([
        ("数形结合", "函数与方程", "related"),
        ("分类讨论", "化归与转化", "related"),
        ("特殊与一般", "归纳与演绎", "related"),
        ("分析法", "综合法", "related"),
        ("直接证明", "间接证明", "related"),
    ])
    
    return relations

def main():
    print("=" * 60)
    print("扩展高中数学知识图谱")
    print("=" * 60)
    
    current_count = get_existing_relations()
    print(f"\n当前关系数: {current_count}")
    
    # 生成并插入更多前置关系
    print("\n生成更多前置关系...")
    additional_prereq = generate_additional_prerequisites()
    print(f"新增前置关系: {len(additional_prereq)} 条")
    insert_knowledge_relations(additional_prereq)
    
    # 生成并插入更多相关关系
    print("\n生成更多相关关系...")
    additional_related = generate_additional_related()
    print(f"新增相关关系: {len(additional_related)} 条")
    insert_knowledge_relations(additional_related)
    
    # 验证结果
    final_count = get_existing_relations()
    print(f"\n最终关系数: {final_count}")
    
    print("\n" + "=" * 60)
    print("知识图谱扩展完成!")
    print("=" * 60)

if __name__ == "__main__":
    main()
