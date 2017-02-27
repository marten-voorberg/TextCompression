def SplitIntoWords(inputString):
    """Split a string into a list of all the words seperated by whitespace"""
    return inputString.split(" ")

def RemoveUppercase(word):
    """Remove the uppercase letters from a word"""
    return word.lower()

def RemovePunctuation(word):
    """Remove punctation characters from the start and the end of a word"""
    # TODO: Refactor checking into a single function
    result = word

    startPunctuationChars = ['(', '{', '[']
    endPunctauationChars = [')', '}', ']', '.', ',', '?', '!', '*']

    firstChar = word[0]
    lastChar = word[len(word) - 1]

    removeFirstChar = False
    removeLastChar = False

    # Check if the first character is a restricted character
    for char in startPunctuationChars:
        if char == firstChar:
            removeFirstChar = True

    # Check if the last character is a restricted character
    for char in endPunctauationChars:
        if char == lastChar:
            removeLastChar = True

    # Remove the first character
    if removeFirstChar:
        result = result[1:]

    # Remove the last character
    if removeLastChar:
        result = result[:-1]

    return result
