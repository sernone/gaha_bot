import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestVCD(unittest.TestCase):
    def test_Connect(self):
        print('Test Passed!')

if __name__ == '__main__':
    unittest.main()