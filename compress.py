import stringManipulation

class Compressor:
    def CountWordOccurences(self, wordArray):
        """Returns a dictionary containing each word in the array and how often it occurs"""
        dict = {}
        for word in wordArray:
            # If the dictionary does not contain the word, add it to the dictionary with 1 occurence
            if not word in dict:
                dict[word] = 1
            else:
                dict[word] += 1

        return dict

def Main():
    compressor = Compressor()
    wordArray = ["the", "quick", "brown", "quick", "brown", "brown"]
    print(compressor.CountWordOccurences(wordArray))

if __name__ == "__main__":
    Main()
