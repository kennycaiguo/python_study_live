"""
argparse built-in module
"""
import argparse
# create the parser
parser = argparse.ArgumentParser(description='命令行中传入一个数字')
parser.add_argument("integer",type=str,help='传入一个数字')
args =parser.parse_args()
print(args)

