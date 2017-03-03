from fileTools import FilePathIntoString
from stringManipulation import CharAtPosIsPunctuationChar, FirstCharIsPunctuationChar, SplitIntoWords
from compress import WordArrayToString

def IsKey(possibleKey):
    if FirstCharIsPunctuationChar(possibleKey):
        return possibleKey[1] == '|'
    else:
        return possibleKey[0] == '|'

def ExtractKey(keyString):
    if FirstCharIsPunctuationChar(keyString):
        return keyString[2:4]
    elif ShouldCapitalizeKey(keyString):
        return keyString[2:4]
    elif ShouldCapitalizeKey(keyString) and FirstCharIsPunctuationChar(keyString):
        return keyString[3:5]
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

def Decompress(inputFilePath, outputFilePath):
    compressedString = FilePathIntoString(inputFilePath)
    dictionary = ExtractTextDictionaryFromString(compressedString)

    compressedWords = SplitIntoWords(compressedString)

    # Remove the dictionary from the first word
    firstWord = compressedWords[0]
    firstWordArray = firstWord.split("\n")
    compressedWords[0] = firstWordArray[len(firstWordArray) - 1]

    # Uncompress Words
    # TODO: Fix uncompressing of words
    for i in range(0, len(compressedWords)):
        word = compressedWords[i]
        if IsKey(word):
            shouldCapitalize = ShouldCapitalizeKey(word)
            extractedKey = ExtractKey(word)
            print(word)
            print(extractedKey)
            if ShouldCapitalizeKey(word):
                uncompressedWord = word.replace(extractedKey, dictionary[extractedKey]).upper()
            else:
                uncompressedWord = word.replace(extractedKey, dictionary[extractedKey])

            uncompressedWord.replace("|", "")
            compressedWords[i] = uncompressedWord

    outputString = WordArrayToString(compressedWords)
    print(outputString)

def Main():
    Decompress("tempIn.txt", "tempOut.txt")
    # ConvertCodeToOriginalWord("")

if __name__ == "__main__":
    Main()