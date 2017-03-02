import stringManipulation
from baseConversion import increment

def CountWordOccurences(wordArray):
    """Returns a dictionary containing each word in the array and how often it occurs"""
    dict = {}
    for word in wordArray:
        # If the dictionary does not contain the word, add it to the dictionary with 1 occurence
        if not word in dict:
            dict[word] = 1
        else:
            dict[word] += 1

    return dict

def FilePathIntoString(filePath):
    with open(filePath, 'r') as file:
        return file.read()

def ConvertWordsInArrayToBaseWords(wordArray):
    """
    Return a word array where the words have been stripped to their basic words
    This includes removing capitalisation and any punctuation characters at the start
    Example: '(Word)' -> 'word'
    """

    # Loop through all the words and remove punctuation and uppercase
    # We use an index because we want to replace the values in the array
    # If we use a foreach array we cannot replace the value in the array
    for i in range(0, len(wordArray)):
        wordArray[i] = stringManipulation.RemovePunctuation(wordArray[i])
        wordArray[i] = stringManipulation.RemoveUppercase(wordArray[i])

    return wordArray

def CalculateCostOfCompressing(word, occurences):
    return (3 + len(word)) + (3 * occurences)

def ShouldCompressWord(word, occurences):
    uncompressedCost = len(word) * occurences
    compressedCost = CalculateCostOfCompressing(word, occurences)
    return compressedCost < uncompressedCost

def CreateDictOfCodeAndWord(wordsWithOccurrencesDict):
    codeAndWordDict = {}

    counter = "00"
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


    for word, occurrence in wordsWithOccurrencesDict.items():
        if ShouldCompressWord(word, occurrence):
            codeAndWordDict[counter] = word

            # Increment the counter by one
            counter = increment(counter, chars)
            # If the length is 1 there should be another 0 in front
            # This is because keys are expected to have a length of 2
            if len(counter) == 1:
                counter = "0" + counter

    return codeAndWordDict

def GenerateDictionaryString(inputDict):
    resultString = ""

    for key, word in inputDict.items():
        resultString += key + word + '\n'

    return resultString

def ReplaceWordsWithCodes(slicedWords, dictOfCompressedWords):
    for i in range(0, len(slicedWords)):
        curWord = slicedWords[i]

        startCharIsPunctuationChar = CharAtPosIsPunctuationChar(curWord, 0)
        endCharIsPunctuationChar = CharAtPosIsPunctuationChar(curWord, len(curWord) - 1)
        startPunctuationChar = ""
        endPunctuationChar = ""

        if startCharIsPunctuationChar:
            startPunctuationChar = curWord[0]

        if endCharIsPunctuationChar:
            endPunctuationChar = curWord[len(curWord) - 1]

        processedWord = stringManipulation.RemovePunctuation(stringManipulation.RemoveUppercase(curWord))

        for key, value in dictOfCompressedWords.items():
            if processedWord == value:
                prefaceChar = "|"
                if WordStartWithUppercase(stringManipulation.RemovePunctuation(curWord)):
                    prefaceChar += '!'
                slicedWords[i] = startPunctuationChar + prefaceChar + key + endPunctuationChar

    return slicedWords

def CharAtPosIsPunctuationChar(word, pos):
    if len(word) == 0:
        return False

    punctuationChars = ['(', '{', '[', ')', '}', ']', '.', ',', '?', '!', '*']
    for punctuaionChar in punctuationChars:
        if punctuaionChar == word[pos]:
            return True

    return False

def WordStartWithUppercase(word):
    if len(word) == 0:
        return False

    firstChar = word[0]
    return word[0] == word[0].upper()

def WordArrayToString(wordArray, separatorChar = " "):
    # Todo: Write tests
    resultString = ""
    for word in wordArray:
        resultString += word + separatorChar

    # Remove last character because it a separatorChar which shouldn't be there
    resultString = resultString[:-1]

    return resultString

def Compress(inputFilePath, outputFilePath):
    originalText = FilePathIntoString(inputFilePath)
    slicedWords = stringManipulation.SplitIntoWords(originalText)
    processedSlicedWords = ConvertWordsInArrayToBaseWords(slicedWords)
    wordsWithOccurences = CountWordOccurences(processedSlicedWords)

    dictOfCompressedWords = CreateDictOfCodeAndWord(wordsWithOccurences)
    dictString = GenerateDictionaryString(dictOfCompressedWords)

    compressedWordsArray = ReplaceWordsWithCodes(slicedWords, dictOfCompressedWords)
    outputString = dictString + WordArrayToString(compressedWordsArray)
    print(outputString)

    # TODO: Write outputString to the outputFilePath

def Main():
    Compress("testFiles/mobydick.txt", "output.txt")

if __name__ == "__main__":
    Main()
