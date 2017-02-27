import unittest
import stringManipulation

class TestSplitIntoWords(unittest.TestCase):
    def testGeneric(self):
        testStr = "The quick brown fox jumps over the lazy dog."
        splitStr = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
        self.assertEqual(stringManipulation.SplitIntoWords(testStr), splitStr)

class TestRemoveUppercase(unittest.TestCase):
    def testFirstLetter(self):
        self.assertEqual(stringManipulation.RemoveUppercase("Word"), "word")

    def testLastLetter(self):
        self.assertEqual(stringManipulation.RemoveUppercase("worD"), "word")

    def testNoLetters(self):
        self.assertEqual(stringManipulation.RemoveUppercase("word"), "word")

    def testAllLetters(self):
        self.assertEqual(stringManipulation.RemoveUppercase("WORD"), "word")

class TestRemovePunctuation(unittest.TestCase):
    def testNoPunctuation(self):
        self.assertEqual(stringManipulation.RemovePunctuation("marten"), "marten")

    def testFirstCharPunctuation(self):
        self.assertEqual(stringManipulation.RemovePunctuation("(marten"), "marten")

    def testLastCharPunctaution(self):
        self.assertEqual(stringManipulation.RemovePunctuation("marten."), "marten")

    def testFirstAndLastCharPunctuation(self):
        self.assertEqual(stringManipulation.RemovePunctuation("(marten)"), "marten")
