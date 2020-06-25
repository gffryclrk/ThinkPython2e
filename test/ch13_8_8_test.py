import unittest
import sys
sys.path.append('ch13/')
import ex_13_8_8 as markov

class TestChooseNWords(unittest.TestCase):
    def setUp(self):
        self.parse_dict = markov.build_dict('text/emma.txt', 3)
        self.od = markov.build_organized_dict(self.parse_dict)

    def testOrderedDict(self):
        """
        Test length of ordered dictionary is correct
        """
        self.assertTrue(len(self.od) == 137448)

    def testChoose_I_shall_press(self):
        """
        Test that words are able to be generated on known positive case
        """
        num_words = 10
        prefix = ('I', 'shall', 'press')
        choose_words = markov.choose_n_words(self.od, prefix, num_words)
        self.assertTrue(len(choose_words) == (num_words + len(prefix)))

    def testLoadMultipleBooks(self):
        """
        Test and see if its possible to load multiple books into a readable dictionary
        """
        self.asserTrue(1 == 1)   # stub


if __name__ == '__main__':
    unittest.main()
