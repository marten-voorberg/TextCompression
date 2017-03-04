from fileTools import FilePathIntoString, WriteToFile
from stringManipulation import CharAtPosIsPunctuationChar, FirstCharIsPunctuationChar, SplitIntoWords
from compress import WordArrayToString

def IsKey(possibleKey):
    if FirstCharIsPunctuationChar(possibleKey):
        return possibleKey[1] == '|'
    else:
        return possibleKey[0] == '|'

def ExtractKey(keyString):
    if ShouldCapitalizeKey(keyString) and FirstCharIsPunctuationChar(keyString):
        return keyString[3:5]
    elif ShouldCapitalizeKey(keyString):
        return keyString[2:4]
    elif FirstCharIsPunctuationChar(keyString):
        return keyString[2:4]
    else:
        return keyString[1:3]

def ShouldCapitalizeKey(keyString):
    if FirstCharIsPunctuationChar(keyString):
        return keyString[2] == "!"
    else:
        return keyString[1] == "!"

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

def UncompressWordArray(compressedWords, dictionary):
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
    Decompress("testFiles/ipsumOut.txt", "testFiles/ipsumOutOut.txt")

if __name__ == "__main__":
    Main()