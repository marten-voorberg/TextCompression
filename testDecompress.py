import unittest
from decompress import *
from fileTools import WriteToFile, FilePathIntoString, DeleteFileContent

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
        self.assertEqual(ExtractKey("|!01"), "01")

    def testCapitalizationAndPunctuation(self):
        self.assertEqual(ExtractKey("(|!01)"), "01")

class TestShouldCapitalizeKey(unittest.TestCase):
    def testNoPunctuationTrue(self):
        self.assertTrue(ShouldCapitalizeKey("|!00"))

    def testNoPunctuationFalse(self):
        self.assertFalse(ShouldCapitalizeKey("|00"))

    def testPunctuationTrue(self):
        self.assertTrue(ShouldCapitalizeKey("(|!00"))

    def testPunctuationFalse(self):
        self.assertFalse(ShouldCapitalizeKey("(|00"))

class TestUncompressWordArray(unittest.TestCase):
    def testEmptyDict(self):
        inputArray = ["This", "is", "a", "sentence."]
        self.assertEqual(UncompressWordArray(inputArray, {}), inputArray)

    def testNoPunctuationAndCapitalization(self):
        inputArray = ["This", "is", "a", "|00"]
        dictionary = {"00": "sentence"}
        expectedOutput = ["This", "is", "a", "sentence"]
        self.assertEqual(UncompressWordArray(inputArray, dictionary), expectedOutput)

    def testOnlyPunctuation(self):
        inputArray = ["This", "is", "a", "(|00)"]
        dictionary = {"00": "sentence"}
        expectedOutput = ["This", "is", "a", "(sentence)"]
        self.assertEqual(UncompressWordArray(inputArray, dictionary), expectedOutput)

    def testOnlyCapitalization(self):
        inputArray = ["This", "is", "a", "|!00"]
        dictionary = {"00": "sentence"}
        expectedOutput = ["This", "is", "a", "Sentence"]
        self.assertEqual(UncompressWordArray(inputArray, dictionary), expectedOutput)

    def testPunctuationAndCapitalization(self):
        inputArray = ["This", "is", "a", "(|!00)"]
        dictionary = {"00": "sentence"}
        expectedOutput = ["This", "is", "a", "(Sentence)"]
        self.assertEqual(UncompressWordArray(inputArray, dictionary), expectedOutput)

class TestDecompress(unittest.TestCase):
    endOfDictString = "|END_OF_DICTIONARY|\n"
    pathToFolder = "testFiles/decompress/"

    def testNoCompression(self):
        inputFile = self.pathToFolder + "noCompressionInput.txt"
        outputFile = self.pathToFolder + "noCompressionOutput.txt"

        input = self.endOfDictString + "This is some normal uncompressed text."
        expectedOutput = "This is some normal uncompressed text."

        WriteToFile(inputFile, input)
        Decompress(inputFile, outputFile)
        actualOutput = FilePathIntoString(outputFile)
        DeleteFileContent(outputFile)
        self.assertEqual(actualOutput, expectedOutput)

    def testNormal(self):
        inputFile = self.pathToFolder + "normalInput.txt"
        outputFile = self.pathToFolder + "normalOutput.txt"

        dictString = "00sentence\n"
        input = dictString + self.endOfDictString + "This is a |!00."
        expectedOutput = "This is a Sentence."

        WriteToFile(inputFile, input)
        Decompress(inputFile, outputFile)
        actualOutput = FilePathIntoString(outputFile)
        DeleteFileContent(outputFile)
        self.assertEqual(actualOutput, expectedOutput)