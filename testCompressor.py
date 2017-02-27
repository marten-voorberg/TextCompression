import unittest
from compress import Compressor

class TestCompressor(unittest.TestCase):
    def testSmallDictionaryWithOnlyOneOccurences(self):
        compressor = Compressor()
        wordArray = ["the", "quick", "brown"]
        expectedDict = { "the": 1, "quick": 1, "brown": 1 }
        self.assertEqual(compressor.CountWordOccurences(wordArray), expectedDict)

    def testSmallDictionaryWithMultipleOccurences(self):
        compressor = Compressor()
        wordArray = ["the", "quick", "brown", "quick", "brown", "brown"]
        expectedDict = { "the": 1, "quick": 2, "brown": 3 }
        self.assertEqual(compressor.CountWordOccurences(wordArray), expectedDict)
