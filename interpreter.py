
# Read homie file
# Translate
# Put result in another python file
# Run

""" 
Translate
    use first word in line as key to which function to translate to
    Translate


"""

INPUT_FILENAME = "syntax.txt"

class Translator:
    def __init__(self, inputFileName :str, outputFileName :str):
        self.file = open(inputFileName, "r")
        self.outputFile = open(outputFileName, "a")
        self.currentLine = ""
        self.currentWordList = ""

    def translate(self):
        print("okay")
        # for every line:
            # use first word in line as key to which func to translate
        
        self.currentLine = self.file.readline()
        self.currentWordList = self.currentLine.split()
        while self.currentLine != "":
            self.varDeclaration()

    def determineWhichStatement(self):
        # bunch of different if statements
        firstWord = self.currentWordList[0]
        if firstWord == "myHomie":
            self.varDeclaration()

    def varDeclaration(self, line :str):
        wordList = line.split(" ")
        outputStr = f"{wordList[0]} = {wordList[2]}"
        self.outputFile.write(outputStr)
        



def main():

    print("OKAY")


main()
