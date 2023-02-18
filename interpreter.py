
# Read homie file
# Translate
# Put result in another python file
# Run

""" 
Translate
    use first word in line as key to which function to translate to
    Translate


"""

INPUT_FILENAME = "inputText.txt"
OUTPUT_FILENAME = "output.py"

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

        for line in self.file:
            print(line)
            self.currentLine = line
            self.currentWordList = self.currentLine.split()
            self.determineWhichStatement()


    def determineWhichStatement(self):
        # bunch of different if statements
        firstWord = self.currentWordList[0]
        if firstWord == "myHomie":
            self.writeVarDeclaration()

    def writeVarDeclaration(self):
        # myHomie i = 100
        outputStr = f"{self.currentWordList[1]} = {self.currentWordList[3]}"
        self.outputFile.write(outputStr)



def main():
    t = Translator(INPUT_FILENAME, OUTPUT_FILENAME)
    t.translate()
    print("OKAY")


main()
