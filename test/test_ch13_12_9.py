"""
Writing some tests for this Zipf thing
"""

import unittest
# import sys
# sys.path.append('ch13/')
from ch13 import ex_13_12_9 as zipf

class TestZipfAnalysis(unittest.TestCase):

    def setUp(self):
        self.haiku_frequencies = zipf.build_freq_dict('text/test_haiku.txt')

    def test_haiku_freqs_greater_than_zero(self):
        """
        Test that the haiku dictionary was loaded
        """

        print(f"Haiku Frequencies Dictionary length: {len(self.haiku_frequencies)}")
        self.assertTrue(len(self.haiku_frequencies) > 0)

        
if __name__ == '__main__':
    unittest.main()
