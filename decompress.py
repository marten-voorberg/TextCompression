from fileTools import FilePathIntoString
from stringManipulation import CharAtPosIsPunctuationChar


def ExtractTextDictionaryFromString(string):
    dictionary = {}
    lines = string.split('\n')
    for line in lines:
        if line == "|END_OF_DICTIONARY|":
            return dictionary

        # The first two characters of the line will be the key
        # The remaining characters will be the word
        dictionary[line[0:2]] = line[2:]

def ConvertCodeToOriginalWord(inputKey, dictionary):
    actualKey = inputKey

    # Check if the first and last char is a punctuation character
    firstCharIsPunctuation = CharAtPosIsPunctuationChar(inputKey, 0)
    lastCharIsPunctuation = CharAtPosIsPunctuationChar(inputKey, len(inputKey) - 1)
    startPuncChar = ""
    endPuncChar = ""
    if firstCharIsPunctuation:
        startPuncChar = inputKey[0]
        actualKey = inputKey[1:]

    if lastCharIsPunctuation:
        endPuncChar = inputKey[len(inputKey) - 1]
        actualKey = inputKey[:-1]

    print(actualKey)

def Decompress(inputFilePath, outputFilePath):
    compressedString = FilePathIntoString(inputFilePath)
    dictionary = ExtractTextDictionaryFromString(compressedString)
    print(dictionary)

def Main():
    # Decompress("tempIn.txt", "tempOut.txt")
    ConvertCodeToOriginalWord("")

if __name__ == "__main__":
    Main()