import unittest
from baseConversion import convert_base_to_dec
from compress import CountWordOccurences, FilePathIntoString, ConvertWordsInArrayToBaseWords, CalculateCostOfCompressing, ShouldCompressWord, CreateDictOfCodeAndWord, GenerateDictionaryString

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

class TestCreateDictOfCodeAndWordDictValues(unittest.TestCase):
    # Todo: test if the keys are incrementing and starting at 0
    def testOneOccurence(self):
        input = {'word': 1}
        self.assertEqual(CreateDictOfCodeAndWord(input), {})

    def testMultipleOccurnces(self):
        input = {'word': 1, 'longword': 10, 'extremelylongword': 10}
        result = CreateDictOfCodeAndWord(input)
        self.assertTrue('longword' in result.values() and 'extremelylongword' in result.values())

    def testCorrectKeys(self):
        # Keys should start at 0 and increment for each word
        # We check if the sum of the keys in the dict is the same as the expected sum
        # The expected sum is equal to adding one number higher to a number each time, starting at 0:
        # 0 + 1 + 2 + 3 + 4 ...
        input = {'word': 1, 'longword': 10, 'extremelylongword': 10}
        result = CreateDictOfCodeAndWord(input)
        amountOfWords = len(result.items())

        expectedCount = 0
        for i in range(0, amountOfWords):
            expectedCount += i

        actualCount = 0
        chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for key in result.keys():
            actualCount += convert_base_to_dec(key, chars)

        self.assertTrue(actualCount == expectedCount)

class TestGenerateDictionaryString(unittest.TestCase):
    def testEmpty(self):
        self.assertEqual(GenerateDictionaryString({}), "")

    def testNonEmpty(self):
        input = {'00': 'longword', '01': 'extremelylongword'}
        self.assertTrue("longword" in GenerateDictionaryString(input) and
                        "extremelylongword" in GenerateDictionaryString(input) and
                        "00" in GenerateDictionaryString(input) and
                        "01" in GenerateDictionaryString(input)
                        )