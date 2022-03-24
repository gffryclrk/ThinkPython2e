"""
Writing some tests for this Zipf thing
"""

import unittest
# import sys
# sys.path.append('ch13/')
from ch13 import ex_13_12_9 as zipf

class TestZipfAnalysis(unittest.TestCase):

    def setUp(self):
        self.emma_frequencies = zipf.build_freq_dict('text/emma.txt')

    def test_emma_freqs_greater_than_zero(self):
        """
        Test that the Emma dictionary was loaded
        """

        print(f"Emma Frequencies Dictionary length: {len(self.emma_frequencies)}")
        self.assertTrue(len(self.emma_frequencies) > 0)

        
if __name__ == '__main__':
    unittest.main()
