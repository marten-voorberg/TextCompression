import unittest
from decompress import *

class TestExtractTextDictionaryFromString(unittest.TestCase):
    def testEmpty(self):
        input ="|END_OF_DICTIONARY|\nsomerandomtextthatisnotimportanthere"
        self.assertEqual(ExtractTextDictionaryFromString(input), {})

    def testNonEmpty(self):
        input = "00word\n01anotherword\n|END_OF_DICTIONARY|\nsomerandomtextthatdoesntmatter"
        expectedOutput = {"00": "word", "01": "anotherword"}
        self.assertEqual(ExtractTextDictionaryFromString(input), expectedOutput)

class TestIsKey(unittest.TestCase):
    def testNoKeyNoPunctuation(self):
        self.assertFalse(IsKey("nokey"))

    def testNoKeyPunctuation(self):
        self.assertFalse(IsKey("(nokey)"))

    def testKeyNoPunctuation(self):
        self.assertTrue(IsKey("|00"))

    def testKeyPunctuation(self):
        self.assertTrue(IsKey("(|00)"))

class TestExtractKey(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(ExtractKey("|01"), "01")

    def testEndPunctuation(self):
        self.assertEqual(ExtractKey("|01)"), "01")

    def testStartPunctuation(self):
        self.assertEqual(ExtractKey("(|01"), "01")

    def testStartAndEndPunctuation(self):
        self.assertEqual(ExtractKey("(|01)"), "01")

    def testCapitalization(self):
        self.assertEqual(ExtractKey("|01"), "01")

    def testCapitalizationAndPunctuation(self):
        self.assertEqual(ExtractKey("(|01)"), "01")

class TestShouldCapitalizeKey(unittest.TestCase):
    def testNoPunctuationTrue(self):
        self.assertTrue(ShouldCapitalizeKey("|!00"))

    def testNoPunctuationFalse(self):
        self.assertFalse(ShouldCapitalizeKey("|00"))

    def testPunctuationTrue(self):
        self.assertTrue(ShouldCapitalizeKey("(|!00"))

    def testPunctuationFalse(self):
        self.assertFalse(ShouldCapitalizeKey("(|00"))