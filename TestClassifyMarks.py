"""Attempted unittesting module."""
import unittest
import classify

class TestClassifyMarks(unittest.TestCase):

    def test_marks_01(self): 
        self.assertEqual(classify.thoseInRange([20, 30], 29, 39), 1)
        self.assertEqual(classify.thoseInRange([20, 40], 29, 39), 0)

    def test_marks_02(self):
        self.assertEqual(classify.thoseInRange([20, -100], 29, 39), 0)
        self.assertEqual(classify.thoseInRange([20, -299], -300, 0), 1)

if __name__ == '__main__':
    unittest.main()
