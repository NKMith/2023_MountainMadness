
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

SYNTAX_DICTIONARY = {
    "var" : "myhomie",
    "def" : "fudge",
    "for" : "fur"
}


class Translator:
    def __init__(self, inputFileName :str, outputFileName :str):
        self.file = open(inputFileName, "r")
        self.outputFile = open(outputFileName, "w+")
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

            outputStr = self.getTab()
            outputStr += self.determineWhichStatement()
            print(outputStr)

            self.outputFile.write(outputStr + '\n')

    def getTab(self):
        tabStr = ""
        count = 0
        while self.currentLine[count] == " ":
            tabStr += " "
            count += 1
        return tabStr

    def determineWhichStatement(self):
        # bunch of different if statements
        firstWord = self.currentWordList[0].lower()
        if firstWord == SYNTAX_DICTIONARY["var"]:
            return self.getVarDeclaration()
        elif firstWord == SYNTAX_DICTIONARY["def"]:
            return self.getFunctionDeclaration()
        
        else:
            return "ERROR - NO SYNTAX MATCHED"

    def getVarDeclaration(self):
        # myHomie i = 100
        print("VAR")
        return f"{self.currentWordList[1]} = {self.currentWordList[3]}"
        
    def getFunctionDeclaration(self):
        #fudge funcName(blah, blah, blah):
        outputStr = "def "
        print(outputStr)
        startInd = len(SYNTAX_DICTIONARY["def"])
        outputStr += self.currentLine[startInd:len(self.currentLine)]
        print(outputStr)
        return outputStr

    def getForDeclaration(self):
        # fur (myhomie i = 0; i < 1; i+=1):
        #fur,(myhomie, i, =, 0;, i, <, 1;, i+=1):
        outputStr = "for "
        outputStr = "i"


    def getEverythingFromCurLineAfterIndex(self, index):
        print()
        
        





def main():
    t = Translator(INPUT_FILENAME, OUTPUT_FILENAME)
    t.translate()
    print("OKAY")


main()
