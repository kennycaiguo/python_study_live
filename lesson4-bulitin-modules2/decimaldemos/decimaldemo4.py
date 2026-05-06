"""
decimal builtin module
"""

"""
进阶应用：结合 logging 进行审计追踪
在金融或关键业务系统中，光算得准还不够，我们还需要记录每一笔计算的详细过程，以便审计和排查问题。这时，我们可以结合 Python 的 logging 模块。

4.1 为什么需要记录计算过程？
当用户投诉“这笔手续费算错了”时，如果你的日志里只有一行 Calculated fee: 0.5，你无法证明它是怎么来的。我们需要记录：

输入参数
使用的精度上下文
中间结果
最终结果
4.2 实战：构建一个带审计日志的计算类
下面是一个结合了 decimal 和 logging 的简单封装示例：
"""

import logging
from decimal import Decimal, getcontext, ROUND_HALF_UP

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

class FinancialCalculator:
    def __init__(self,precision=4):
        self.precision = precision
        # 设置局部上下文
        getcontext().prec = precision + 2 # 计算过程保留更多位数，防止中间误差
        getcontext().rounding = ROUND_HALF_UP
        logger.info(f"计算器初始化，精度设置为: {precision}")
    
    def calc_tax(self,amount,rate):
        """
        计算税额
        :param amount: 金额 (Decimal or str)
        :param rate: 税率 (Decimal or str)
        """
        # 强制转换为 Decimal，并记录输入
        amt = Decimal(str(amount))
        rt = Decimal(str(rate))
        logger.info(f"开始计算税额 | 输入金额: {amt}, 税率: {rt}")
        # 计算原始值
        tax = amt * rt
        logger.debug(f"原始计算结果: {tax}")
        # 最终舍入
        final_tax = tax.quantize(Decimal('0.01'))
        logger.info(f"计算完成 | 税额: {final_tax}")
        return final_tax
    
calc = FinancialCalculator(precision=6)
tax = calc.calc_tax('1234.56', '0.08')    




