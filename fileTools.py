def FilePathIntoString(filePath):
    with open(filePath, 'r') as file:
        return file.read()

def DeleteFileContent(filePath):
    with open(filePath, "w"):
        pass

def WriteToFile(filePath, string):
    with open(filePath, 'w') as file:
        file.write(string)