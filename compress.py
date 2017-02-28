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

def Compress(inputFilePath, outputFilePath):
    originalText = FilePathIntoString(inputFilePath)
    slicedWords = stringManipulation.SplitIntoWords(originalText)
    processedSlicedWords = ConvertWordsInArrayToBaseWords(slicedWords)
    wordsWithOccurences = CountWordOccurences(processedSlicedWords)

    dictOfCompressedWords = CreateDictOfCodeAndWord(wordsWithOccurences)
    dictString = GenerateDictionaryString(dictOfCompressedWords)

    # Replace the word in the original text with the code
    print(slicedWords)
    for i in range(0, len(slicedWords)):
        curword = slicedWords[i]
        processedWord = stringManipulation.RemovePunctuation(stringManipulation.RemoveUppercase(curword))
        for key, word in dictOfCompressedWords.items():
            if word == curword:
                slicedWords[i] = key
                # if curword[0] == curword[0].upper():
                #     slicedWords[i] = '!' + key
                # else:
                #     slicedWords[i] = key

    res = ""
    for word in slicedWords:
        res += word + ' '
    print(res)

    # print(wordsWithOccurences)
    # print(dictString)

def Main():
    Compress("testFiles/mobydick.txt", "output.txt")

if __name__ == "__main__":
    Main()
