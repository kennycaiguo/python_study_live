"""
argparse built-in module
"""
import argparse
# # create the parser
# parser = argparse.ArgumentParser(description='命令行中传入一个数字')
# parser.add_argument("integer",type=str,help='传入一个数字')
# args =parser.parse_args()
# print(args)
# #获得integer参数
# print(args.integer)

## 注意，上面的脚本只能够接收一个命令行参数，如果需要接收多个命令行参数，需要修改代码如下
# create the parser
# parser = argparse.ArgumentParser(description='命令行中传入一个数字')
# parser.add_argument("integer",type=str,nargs='+',help='传入一个数字')
# args =parser.parse_args()
# print(args)

## demo3
# 1. 定义命令行解析器对象
# parser = argparse.ArgumentParser(description='Demo of argparse')
 
# # 2. 添加命令行参数
# parser.add_argument('--epochs', type=int, default=30)
# parser.add_argument('--batch', type=int, default=4)
 
# # 3. 从命令行中结构化解析参数 # 调用方法： python .\argparserdemo.py --epochs=20 --batch=3
# args = parser.parse_args()
# print(args)
# epochs = args.epochs
# batch = args.batch
# print('Args: {}  {}'.format(epochs, batch))

# # demo4 # 调用方法  python .\argparserdemo.py 127.0.0.1  --port=80  或者 python .\argparserdemo.py 127.0.0.1  因为端口设置了默认值
# # 创建解析器 
# parser = argparse.ArgumentParser(description="端口扫描器")

# # 添加位置参数（IP地址）
# parser.add_argument('ip', type=str, help="目标IP地址")

# # 添加可选参数（端口号）
# parser.add_argument('--port', type=int, default=80, help="指定端口号")

# # 解析参数
# args = parser.parse_args()

# # 输出解析结果
# print(f"扫描目标: {args.ip}")
# print(f"端口号: {args.port}")

# demo5 # 调用方法：python .\argparserdemo.py --level=3,当你的level的值不是choices里面的数字，就会抛异常

parser = argparse.ArgumentParser(description="限制参数范围")
parser.add_argument('--level', type=int, choices=[1, 2, 3], help="选择级别")
args = parser.parse_args()

print(f"选择的级别是 {args.level}")