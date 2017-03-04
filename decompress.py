import sys
from fileTools import FilePathIntoString, WriteToFile
from stringManipulation import CharAtPosIsPunctuationChar, FirstCharIsPunctuationChar, SplitIntoWords
from compress import WordArrayToString

def IsKey(possibleKey):
    """Return if a certain string is a key. This will be marked by a '|'. Somtimes there's a punctuation character before it. The '|' will then be the 2 character"""
    if FirstCharIsPunctuationChar(possibleKey):
        return possibleKey[1] == '|'
    else:
        return possibleKey[0] == '|'

def ExtractKey(keyString):
    """Extract the key from a keyString. This is neccesary because there will always be a '|' and sometimes a '!' or punctuation character."""
    if ShouldCapitalizeKey(keyString) and FirstCharIsPunctuationChar(keyString):
        return keyString[3:5]
    elif ShouldCapitalizeKey(keyString):
        return keyString[2:4]
    elif FirstCharIsPunctuationChar(keyString):
        return keyString[2:4]
    else:
        return keyString[1:3]

def ShouldCapitalizeKey(keyString):
    """Return if the word that this key resembles should be uppercase. This is marked by a '!' after the '|'"""
    if FirstCharIsPunctuationChar(keyString):
        return keyString[2] == "!"
    else:
        return keyString[1] == "!"

def ExtractTextDictionaryFromString(string):
    dictionary = {}
    lines = string.split('\n')

    # Keep adding to the dictionary until we hit the end of the dictionary marked by the end of dictionary line
    for line in lines:
        if line == "|END_OF_DICTIONARY|":
            return dictionary

        # The first two characters of the line will be the key
        # The remaining characters will be the word
        key = line[0:2]
        word = line[2:]
        dictionary[key] = word

def UncompressWordArray(compressedWords, dictionary):
    """Returns a wordArray where the compressedWords have been replaced by the uncompressedWords"""
    for i in range(0, len(compressedWords)):
        curWord = compressedWords[i]
        if IsKey(curWord):
            extractedKey = ExtractKey(curWord)
            keyChars = "|"

            dictEntry = dictionary[extractedKey]
            if ShouldCapitalizeKey(curWord):
                keyChars += "!"
                dictEntry = dictEntry.capitalize()

            uncompressedWord = curWord.replace((keyChars + extractedKey), dictEntry)
            compressedWords[i] = uncompressedWord

    return compressedWords

def Decompress(inputFilePath, outputFilePath):
    """Decompress the input file and write the result to the output file"""
    # TODO: Add tests for this function
    compressedString = FilePathIntoString(inputFilePath)
    dictionary = ExtractTextDictionaryFromString(compressedString)

    compressedWords = SplitIntoWords(compressedString)

    # Remove the dictionary from the first word
    firstWord = compressedWords[0]
    firstWordArray = firstWord.split("\n")
    compressedWords[0] = firstWordArray[len(firstWordArray) - 1]

    uncompressedWords = UncompressWordArray(compressedWords, dictionary)
    outputString = WordArrayToString(uncompressedWords)
    WriteToFile(outputFilePath, outputString)

def Main():
    inputFilePath = sys.argv[1]
    outputFilePath = sys.argv[2]
    Decompress(inputFilePath, outputFilePath)


if __name__ == "__main__":
    Main()