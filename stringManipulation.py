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
    endPunctauationChars = [')', '}', ']', '.', ',', '?', '!', '*']

    firstChar = word[0]
    lastChar = word[len(word) - 1]

    # If the list of restricted punctuation characters contains the first characters
    # this sets the boolean to true, otherwise false
    removeFirstChar = ListContainsItem(startPunctuationChars, firstChar)
    removeLastChar = ListContainsItem(endPunctauationChars, lastChar)

    # Remove the first character
    if removeFirstChar:
        result = result[1:]

    # Remove the last character
    if removeLastChar:
        result = result[:-1]

    return result
