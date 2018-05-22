import unittest
import classify

class TestClassifyMarks(unittest.TestCase):

    def test_marks_01(self): 
        self.assertEqual(classify.thoseInRange((1, 30), 29, 39), 1)
        self.assertEqual(classify.thoseInRange((2, 40), 29, 39), 0)

if __name__ == '__main__':
    unittest.main()
