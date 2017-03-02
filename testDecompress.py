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