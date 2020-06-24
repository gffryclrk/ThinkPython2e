import unittest
import sys
sys.path.append('ch13/')
import ex_13_8_8 as markov

class TestChooseNWords(unittest.TestCase):
    def setUp(self):
        self.od = markov.build_dict('text/emma.txt', 3)

    def testOrderedDict(self):
        self.assertTrue(len(self.od) == 137448)

if __name__ == '__main__':
    unittest.main()
