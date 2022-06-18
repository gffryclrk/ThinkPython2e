""" Testing Kangaroo exercises in Chapter 17 
Section 13"""
import unittest
from ch17.kangaroo import Kangaroo


class TestKangaroo(unittest.TestCase):

    def setUp(self):
        self.kanga = Kangaroo()
        self.roo = Kangaroo()

    def test_add_roo_to_kangas_pouch(self):
        """    Test your code by creating two Kangaroo objects, assigning them to variables named kanga and
    roo, and then adding roo to the contents of kanga’s pouch."""

        self.kanga.put_in_pouch(self.roo)

        print(self.kanga)
