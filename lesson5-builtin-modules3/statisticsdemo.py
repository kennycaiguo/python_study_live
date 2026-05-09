import statistics as stats

def demo1():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 算术平均数
    mean = stats.mean(data)
    print(f"平均数: {mean}")  # 5

    # 中位数
    median = stats.median(data)
    print(f"中位数: {median}")  # 5

    # 众数
    data2 = [1, 2, 2, 3, 4, 4, 4, 5]
    mode = stats.mode(data2)
    print(f"众数: {mode}")  # 4

    # 分位数
    quartiles = stats.quantiles(data, n=4)
    print(f"四分位数: {quartiles}")  # [2.5, 5.0, 7.5]

def demo2():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 方差
    variance = stats.variance(data)
    print(f"方差: {variance}")  # 7.5

    # 标准差
    stdev = stats.stdev(data)
    print(f"标准差: {stdev}")  #  2.7386127875258306

    # 总体方差和标准差
    pvariance = stats.pvariance(data)
    pstdev = stats.pstdev(data)
    print(f"总体方差: {pvariance}, 总体标准差: {pstdev}") # 总体方差: 6.666666666666667, 总体标准差: 2.581988897471611

def demo3():
    # 调和平均数
    harmonic_mean = stats.harmonic_mean([1, 2, 4])
    print(f"调和平均数: {harmonic_mean}")  #  1.7142857142857142

    # 几何平均数
    geometric_mean = stats.geometric_mean([1, 2, 4])
    print(f"几何平均数: {geometric_mean}")  # 2.0

    # 协方差和相关系数
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    covariance = stats.covariance(x, y)
    correlation = stats.correlation(x, y)
    print(f"协方差: {covariance}, 相关系数: {correlation}")  # 协方差: 5.0, 相关系数: 1.0  

def stu_score_demo():
    import statistics as stats

    # 学生成绩数据
    scores = [85, 92, 78, 96, 88, 76, 91, 84, 79, 87]

    # 基本统计信息
    print(f"平均分: {stats.mean(scores):.2f}")
    print(f"中位数: {stats.median(scores)}")
    print(f"最高分: {max(scores)}")
    print(f"最低分: {min(scores)}")
    print(f"分数范围: {max(scores) - min(scores)}")
    print(f"标准差: {stats.stdev(scores):.2f}")

    # 成绩分布分析
    q1, q2, q3 = stats.quantiles(scores, n=4)
    print(f"第一四分位数 (Q1): {q1}")
    print(f"第二四分位数 (中位数, Q2): {q2}")
    print(f"第三四分位数 (Q3): {q3}")
    print(f"四分位距 (IQR): {q3 - q1}")    

def detect_outliers(data):
    """使用IQR方法检测异常值"""
    q1, q3 = stats.quantiles(data, n=4)[0], stats.quantiles(data, n=4)[2]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    return outliers

def test_detect_outliers():
    """数据异常值检测案例"""
    # 测试数据（包含一个异常值）
    test_data = [10, 12, 12, 13, 12, 11, 14, 13, 15, 10, 50]
    outliers = detect_outliers(test_data)
    print(f"异常值: {outliers}")  # 异常值: [50]


# 计算基本统计量
def analyze_returns(returns, name):
    print(f"\n{name}分析:")
    print(f"平均收益率: {stats.mean(returns):.3f}")
    print(f"收益率标准差: {stats.stdev(returns):.3f}")
    print(f"收益率方差: {stats.variance(returns):.6f}")

def test_analyze_returns():
    # 模拟两只股票的收益率
    stock_a_returns = [0.02, 0.03, -0.01, 0.05, 0.02]
    stock_b_returns = [0.01, 0.04, 0.02, -0.02, 0.03]
    
    analyze_returns(stock_a_returns, "股票A")
    analyze_returns(stock_b_returns, "股票B")

    # 计算相关性
    corr = stats.correlation(stock_a_returns, stock_b_returns)
    print(f"\n两只股票的相关系数: {corr:.3f}")

def error_handle():
    import statistics as stats

    # 处理空数据
    try:
        empty_data = []
        result = stats.mean(empty_data)
    except stats.StatisticsError as e:
        print(f"错误: {e}")

    # 处理单一数据点
    single_point = [5]
    try:
        result = stats.stdev(single_point)
    except stats.StatisticsError as e:
        print(f"错误: {e}")  # 需要至少两个数据点来计算标准差
    """
    错误: mean requires at least one data point
    错误: stdev requires at least two data points
    """    

def compare_with_numpy():
    """与第三方库对比numpy"""    
    import statistics as stats
    import numpy as np

    data = [1, 2, 3, 4, 5]

    # statistics 模块
    stats_mean = stats.mean(data)
    stats_std = stats.stdev(data)

    # NumPy
    np_mean = np.mean(data)
    np_std = np.std(data, ddof=1)  # ddof=1 对应样本标准差

    print(f"statistics - 均值: {stats_mean}, 标准差: {stats_std}")
    print(f"NumPy - 均值: {np_mean}, 标准差: {np_std}")

    """
    statistics - 均值: 3, 标准差: 1.5811388300841898
    NumPy - 均值: 3.0, 标准差: 1.5811388300841898
    """

if __name__ == '__main__':
    # demo1()    
    # demo2()    
    # demo3()    
    # stu_score_demo()
    # test_detect_outliers()
    # test_analyze_returns()
    # error_handle()
    compare_with_numpy()
