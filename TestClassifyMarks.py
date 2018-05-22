import unittest
import classifymarks

class TestClassifyMarks(unittest.TestCase):

    def test_marks_01(self): 
        self.AssertEqual(classifymarks.thoseInRange((AB0001, 30), 29, 39), 1)
        self.AssertEqual(classifymarks.thoseInRange((AB0002, 40), 29, 39), 0)

if __name__ == '__main__':
    unittest.main()
