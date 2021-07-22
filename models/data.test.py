import unittest
from data import Data

class TestDataMethods(unittest.TestCase):

    def test_init(self):
        data = Data("06182660000E1E00FAFF34")

if __name__ == '__main__':
    unittest.main()