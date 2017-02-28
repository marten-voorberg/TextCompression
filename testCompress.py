import unittest
from compress import CountWordOccurences, FilePathIntoString, ConvertWordsInArrayToBaseWords, CalculateCostOfCompressing, ShouldCompressWord

class TestCountWordOccurences(unittest.TestCase):
    def testSmallDictionaryWithOnlyOneOccurences(self):
        wordArray = ["the", "quick", "brown"]
        expectedDict = { "the": 1, "quick": 1, "brown": 1 }
        self.assertEqual(CountWordOccurences(wordArray), expectedDict)

    def testSmallDictionaryWithMultipleOccurences(self):
        wordArray = ["the", "quick", "brown", "quick", "brown", "brown"]
        expectedDict = { "the": 1, "quick": 2, "brown": 3 }
        self.assertEqual(CountWordOccurences(wordArray), expectedDict)

class TestFilePathIntoString(unittest.TestCase):
    def testNormalFile(self):
        expectedString = "This is a sentence."
        self.assertEqual(FilePathIntoString("testFiles/smallText.txt"), expectedString)

    # Todo: fix this test
    # def testNonExistentFile(self):
    #    self.failUnlessRaises(IOError, FilePathIntoString("non-existent-file-path"))

class TestConvertWordsInArrayToBaseWords(unittest.TestCase):
    def testOnlyPunctuation(self):
        inputArray = ["word.", "(santa)", "john"]
        expectedOutput = ["word", "santa", "john"]
        self.assertEqual(ConvertWordsInArrayToBaseWords(inputArray), expectedOutput)

    def testOnlyUppercase(self):
        inputArray = ["Word", "santa", "John"]
        expectedOutput = ["word", "santa", "john"]
        self.assertEqual(ConvertWordsInArrayToBaseWords(inputArray), expectedOutput)

    def testUppercaseAndPunctuation(self):
        inputArray = ["Word", "santa.", "(John)"]
        expectedOutput = ["word", "santa", "john"]
        self.assertEqual(ConvertWordsInArrayToBaseWords(inputArray), expectedOutput)

class TestCalculateCostOfCompressing(unittest.TestCase):
    def testWordWithOneOccurrence(self):
        self.assertEqual(
            CalculateCostOfCompressing('word', 1),
            10
        )

    def testWordWithMultipleOccurences(self):
        self.assertEqual(
            CalculateCostOfCompressing('longword', 10),
            41
        )

class TestShouldCompressWord(unittest.TestCase):
    def testSingleOccurenceFalse(self):
        self.assertFalse(ShouldCompressWord("word", 1))

    def testMultipleOccurenceFalse(self):
        self.assertFalse(ShouldCompressWord("word", 2))

    def testMultipleOccurenceTrue(self):
        self.assertTrue(ShouldCompressWord("longword", 10))