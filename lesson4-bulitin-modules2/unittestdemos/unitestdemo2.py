"""
python uinttest built-in module
"""

import unittest

class MyTest(unittest.TestCase):
    
    def setUp(self):
        print("Begin...")  
        number = input("please enter a number: ")
        self.number = int(number)
    def test_1(self):
        print(self.number)
        self.assertEqual(self.number,10,msg='The number needed is 10')

    def test_2(self):
        print(self.number)
        self.assertEqual(self.number,20,msg='The number needed is 20') 

    def tearDown(self):
       print("End...")

    
    
if __name__ == '__main__':
    unittest.main()    # you don't have to deal with the class yourself,just call unittest.main()

'''
Begin...
please enter a number: 10
10
End...
.Begin...
please enter a number: 20
20
End...
.
----------------------------------------------------------------------
Ran 2 tests in 4.423s

OK

''' 