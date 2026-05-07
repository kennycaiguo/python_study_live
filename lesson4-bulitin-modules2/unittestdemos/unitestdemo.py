"""
python uinttest built-in module
"""

import unittest

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("UnitTest Begin...")

    @classmethod
    def tearDownClass(self):
       print("UnitTest End...")

    def setUp(self):
        print("Begin...")  

    def tearDown(self):
       print("End...")

    def test_1(self):
        self.assertEqual(1,1)
    def test_2(self):
        self.assertEqual(1,2)   
    
if __name__ == '__main__':
    unittest.main()    # you don't have to deal with the class yourself,just call unittest.main()

"""
UnitTest Begin...
Begin...
End...
.Begin...
FEnd...
UnitTest End...

======================================================================
FAIL: test_2 (__main__.MyTest.test_2)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\pc_programming_live\python_study_live\lesson4-bulitin-modules2\unitestdemo.py", line 25, in test_2
    self.assertEqual(1,2)
AssertionError: 1 != 2

----------------------------------------------------------------------
Ran 2 tests in 0.002s

FAILED (failures=1)
"""    