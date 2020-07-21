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

class TestAnagramSetGenerator(unittest.TestCase):

    def __init__(self):
        self.test_file_dir = 'tmp'
        self.test_file_path = f'{test_file_dir}/anagrams'
        self.sample_anagrams = [
            ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled'],
            ['retainers', 'ternaries'],
            ['generating', 'greatening'],
            ['resmelts', 'smelters', 'termless']
        ]

    def setUp(self):

        Path(self.test_file_dir).mkdir(parents=True, exist_ok=True)
        f = open(self.test_file_path, 'w')
        for line in sample_anagrams:
            f.write(' '.join(line) + '\n')

        f.close()


    def test_build_anagram_dict(self):
        """Test anagram file written in setUp can be read using generator and method from implementation"""

        tmp_gen = ag.word_gen(self.test_file_path)
        anagram_dict = ag.build_anagram_dict(tmp_gen)
        self.assertTrue(len(self.sample_anagrams) == len(anagram_dict))


if __name__ == '__main__':
    unittest.main()
        
