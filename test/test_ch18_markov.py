from unittest.mock import patch, call
import unittest
from ch18.markov import main
import pdb

class TestMarkov(unittest.TestCase):

    @patch('builtins.print')
    def test_main(self, mock_print):

        n = 100
        # with patch('builtins.print') as mock_print:
        main('markov.py', 'text/emma.txt', n, 2)

        self.assertTrue(len(mock_print.call_args_list) >= n)
