import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def testAdd(self): 
        cal = Calculator()
        result = cal.add(10,2)
        self.assertEqual(result,12)
    def testSub(self):
        cal = Calculator()
        result = cal.sub(10,2)
        self.assertEqual(result,8)
    def testMul(self):
        cal = Calculator()
        result = cal.mul(10,2)
        self.assertEqual(result,20)
    def testDivide(self):
        cal = Calculator()
        result = cal.div(10,2)
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()
