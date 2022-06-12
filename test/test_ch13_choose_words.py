import unittest
import sys
sys.path.append('ch13/')
import ex_13_8_8 as markov

class TestChooseNWords(unittest.TestCase):

    def setUp(self):
        gen = markov.read_file('text/emma.txt', 3, 249)
        self.parse_dict = markov.build_dict(gen)
        self.od = markov.build_organized_dict(self.parse_dict)

    def test_ordered_dict(self):
        """
        re-run generator and ensure every prefix is in dict
        """
        emma_gen = markov.read_file('text/emma.txt', 3, 249)
        for prefix in emma_gen:
            if prefix[0] not in self.od: print(f'prefix {prefix[0]} not found in od')
            self.assertTrue(prefix[0] in self.od)
            
#        self.assertTrue(len(self.od) == 137448)

    def test_choose_I_shall_press(self):
        """
        Test that words are able to be generated on known positive case
        """
        num_words = 10
        prefix = ('I', 'shall', 'press')
        choose_words = markov.choose_n_words(self.od, prefix, num_words)
        self.assertTrue(len(choose_words) == (num_words + len(prefix)))

    def test_load_multiple_books(self):
        """
        Test load multiple books into pre-generated dictionary
        """

        prefix1 = ('A', 'SCANDAL', 'IN') 
        prefix2 = ('SCANDAL', 'IN', 'BOHEMIA')

        mash_up = self.od
        self.assertFalse(prefix1 in mash_up or prefix2 in mash_up)

        sherlock_gen = markov.read_file('text/sherlock_1661-0.txt', 3, 58)
        mash_up = markov.build_dict(sherlock_gen, self.parse_dict)

        self.assertTrue(prefix1 in mash_up and prefix2 in mash_up)
        


if __name__ == '__main__':
    unittest.main()
