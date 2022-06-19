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

    def __init__(self, contents=[]):
       """In his example the author includes an empty list as a default argument which
       is a "dangerous-default-value" in python. This is because a mutable default value
       will keep its mutable state on subsequent method/function calls.

       Thus in the author's example the empty list keeps the contents for both instances of
       the Kangaroo class. However, since I didn't use a mutable data structure as a default
       arg I didn't have the same issue."""
       self.pouch_contents = contents

    def put_in_pouch(self, object):
        self.pouch_contents.append(object) 

    def __str__(self):
        return "Pouch contents: {}".format(self.pouch_contents)

if __name__ == '__main__':
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch(roo)
    kanga.put_in_pouch("wallet")
    print("--kanga contents--")
    print(kanga.pouch_contents)
    print("--roo contents--")
    print(roo.pouch_contents)
