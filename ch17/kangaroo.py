"""17.13 Exercises
    Exercise 17.7. This exercise is a cautionary tale about one of the most common, and difficult to
    find, errors in Python. Write a definition for a class named Kangaroo with the following methods:
    1. An __init__ method that initializes an attribute named pouch_contents to an empty list.
    2. A method named put_in_pouch that takes an object of any type and adds it to
    pouch_contents.
    3. A __str__ method that returns a string representation of the Kangaroo object and the con-
    tents of the pouch.
    Test your code by creating two Kangaroo objects, assigning them to variables named kanga and
    roo, and then adding roo to the contents of kanga’s pouch.
"""

class Kangaroo:
    """For test 3 above, see test_add_roo_to_kangas_pouch in ../test/test_ch_17_13_kangaroo.py"""

    def __init__(self):
       self.pouch_contents = [] 

    def put_in_pouch(self, object):
        self.pouch_contents.append(object) 

    def __str__(self):
        return "Pouch contents: {}".format(self.pouch_contents)

if __name__ == '__main__':
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch(roo)
    print(kanga.pouch_contents)
