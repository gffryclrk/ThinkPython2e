"""Unit tests for Exercise 12.10.2: Anagram Sets

pathlib.Path.mkdir used to create tmp directorty if necessary,
requries Python >= 3.5.
https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory

"""

import unittest
import sys
sys.path.append('ch12/')
import ex12_10_2_redo as ag
from pathlib import Path

class TestAnagramSets(unittest.TestCase):

    test_file_dir = 'tmp'
    test_file_path = f'{test_file_dir}/anagrams'
    sample_anagrams = [
        ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled'],
        ['retainers', 'ternaries'],
        ['generating', 'greatening'],
        ['resmelts', 'smelters', 'termless']
    ]

    def setUp(self):

        Path(self.test_file_dir).mkdir(parents=True, exist_ok=True)
        f = open(self.test_file_path, 'w')
        for line in self.sample_anagrams:
            f.write(' '.join(line) + '\n')

        f.close()
        
        tmp_gen = ag.word_gen(self.test_file_path)
        self.anagram_dict = ag.build_anagram_dict(tmp_gen)


    def test_build_anagram_dict(self):
        """Test anagram file written in setUp can be read using generator and method from implementation"""

        self.assertTrue(len(self.sample_anagrams) == len(self.anagram_dict))

    def test_anagram_in_proper_value_for_key(self):
        """Check and make sure values of each list are in list with same key"""
        for list in self.sample_anagrams:
            key = tuple(sorted(list[0]))

            sample_set = set(list)
            dict_set = set(self.anagram_dict[key])
            self.assertTrue(len(sample_set - dict_set) == 0)

if __name__ == '__main__':
    unittest.main()
        
