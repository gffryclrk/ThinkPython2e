import unittest
import sys
sys.path.append('ch13/')
import ex_13_8_8 as markov

class TestChooseNWords(unittest.TestCase):
    def setUp(self):
        gen = markov.read_file('text/emma.txt', 3, 249)
        self.parse_dict = markov.build_dict(gen)
        self.od = markov.build_organized_dict(self.parse_dict)

    def testOrderedDict(self):
        """
        Test length of ordered dictionary is correct
        """
        print(f"len of self.od: {len(self.od)}")
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
        Test load multiple books into pre-generated dictionary
        """

        prefix1 = ('A', 'SCANDAL', 'IN') 
        prefix2 = ('SCANDAL', 'IN', 'BOHEMIA')

        mash_up = self.od
        self.assertFalse(prefix1 in mash_up or prefix2 in mash_up)

        sherlock_gen = markov.read_file('text/sherlock_1661-0.txt', 3, 249)
        mash_up = markov.build_dict(sherlock_gen, self.parse_dict)

        self.assertTrue(prefix1 in self.parse_dict and prefix2 in self.parse_dict)
        


if __name__ == '__main__':
    unittest.main()
