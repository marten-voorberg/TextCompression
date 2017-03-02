import unittest
from fileTools import *


class TestFilePathIntoString(unittest.TestCase):
    def testNormalFile(self):
        expectedString = "This is a sentence."
        self.assertEqual(FilePathIntoString("testFiles/fileToRead.txt"), expectedString)

    # Todo: fix this test
    # def testNonExistentFile(self):
    #    self.failUnlessRaises(IOError, FilePathIntoString("non-existent-file-path"))

class TestDeleteFileContent(unittest.TestCase):
    def testNormalFile(self):
        # Check if the file is not empty to begin with
        filePath = "testFiles/fileToDelete.txt"
        nonEmptyContent = "This should get deleted by test."
        contentAtStart = FilePathIntoString(filePath)
        if nonEmptyContent != contentAtStart:
            raise ValueError('Test file should be equal to the non empty filler content. Currently is: "' + contentAtStart + '". Should be: ' + nonEmptyContent)

        DeleteFileContent(filePath)

        contentAfterDeletion = FilePathIntoString(filePath)

        # Add filler content so test is repeatable
        with open(filePath, 'w') as file:
            file.write(nonEmptyContent)

        self.assertEqual(contentAfterDeletion, "")

class TestWriteToFile(unittest.TestCase):
    def testNormalFile(self):
        filePath = "testFiles/fileToWriteTo.txt"
        string = "This is the string that should be written"

        # Delete any content currently in file:
        DeleteFileContent(filePath)

        # Write to file
        WriteToFile(filePath, string)

        read = FilePathIntoString(filePath)

        self.assertEqual(read, string)

