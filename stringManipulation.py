from listTools import ListContainsItem

def SplitIntoWords(inputString):
    """Split a string into a list of all the words seperated by whitespace"""
    return inputString.split(" ")

def RemoveUppercase(word):
    """Remove the uppercase letters from a word"""
    return word.lower()

def RemovePunctuation(word):
    """Remove punctation characters from the start and the end of a word"""
    result = word

    startPunctuationChars = ['(', '{', '[']
    endPunctuationChars = [')', '}', ']', '.', ',', '?', '!', '*']

    firstChar = word[0]
    lastChar = word[len(word) - 1]

    # If the list of restricted punctuation characters contains the first characters
    # this sets the boolean to true, otherwise false
    shouldRemoveFirstChar = ListContainsItem(startPunctuationChars, firstChar)
    shouldRemoveLastChar = ListContainsItem(endPunctuationChars, lastChar)

    # Remove the first character
    if shouldRemoveFirstChar:
        result = result[1:]

    # Remove the last character
    if shouldRemoveLastChar:
        result = result[:-1]

    return result

def CharAtPosIsPunctuationChar(word, pos):
    if len(word) == 0:
        return False

    punctuationChars = ['(', '{', '[', ')', '}', ']', '.', ',', '?', '!', '*']
    for punctuaionChar in punctuationChars:
        if punctuaionChar == word[pos]:
            return True

    return False