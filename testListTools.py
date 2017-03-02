import unittest
from listTools import ListContainsItem

class TestListContainsItem(unittest.TestCase):
    def testIntInListOfInts(self):
        list = [2, 4, 6]
        num = 4
        self.assertTrue(ListContainsItem(list, num))

    def testCharInListOfInts(self):
        list = [2, 4, 6]
        char ='a'
        self.assertFalse(ListContainsItem(list, char))

    def testCharInListOfChars(self):
        list = ['a', 'b', 'c']
        char = 'a'
        self.assertTrue(ListContainsItem(list, char))

    def testCharInString(self):
        string = "abc"
        char = "a"
        self.assertTrue(ListContainsItem(string, char))

    def testCharNotInString(self):
        string = "abc"
        char = 'z'
        self.assertFalse(ListContainsItem(string, char))
