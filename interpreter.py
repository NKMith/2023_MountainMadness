
# Read homie file
# Translate
# Put result in another python file
# Run

""" 
Translate
    use first word in line as key to which function to translate to
    Translate


"""

INPUT_FILENAME = "inputCode.txt"
OUTPUT_FILENAME = "output.py"

SYNTAX_DICTIONARY = {
    "var" : "myhomie",
    "def" : "fudge",
    "for" : "fur",
    "print" : "gundam",
    "input" : "whatDoYouWant"
}


class Translator:
    def __init__(self, inputFileName :str, outputFileName :str):
        self.file = open(inputFileName, "r")
        self.outputFile = open(outputFileName, "w+")

        self.currentLine = ""
        self.processingLine = ""
        self.currentWordList = ""

    def removeNewlineFromProcessedLine(self):
        if self.processingLine[len(self.processingLine)-1] == '\n':
            self.processingLine = self.processingLine[0:len(self.processingLine)-1]

    def removeTab(self):
        count = self.countTab()
        self.processingLine = self.processingLine[count:len(self.processingLine)]

    def countTab(self):
        count = 0
        while self.currentLine[count] == " ":
            count += 1
        return count

    def translate(self):
        print("okay")
        # for every line:
            # use first word in line as key to which func to translate

        for line in self.file:
            if line == "\n":
                continue #TODO - Try to get rid of this

            self.currentLine = line
            self.processingLine = line
            self.removeNewlineFromProcessedLine()
            self.removeTab()
            self.currentWordList = self.currentLine.split()

            outputStr = self.getTab()
            self.determineWhichStatement()
            outputStr += self.processingLine
            print("WRITING STR: " + outputStr)

            self.outputFile.write(outputStr + '\n')

    def getTab(self):
        count = self.countTab()
        return self.currentLine[0:count]

    def determineWhichStatement(self):
        # bunch of different if statements
        if SYNTAX_DICTIONARY["print"] in self.processingLine:
            self.processingLine = self.processingLine.replace(SYNTAX_DICTIONARY["print"], "print")

        if SYNTAX_DICTIONARY["input"] in self.processingLine:
            self.processingLine = self.processingLine.replace(SYNTAX_DICTIONARY["input"], "input")


        firstWord = self.currentWordList[0].lower()
        if firstWord == SYNTAX_DICTIONARY["var"]:
            self.getVarDeclaration()
        elif firstWord == SYNTAX_DICTIONARY["def"]:
            self.getFunctionDeclaration()


    def getVarDeclaration(self):
        # myHomie i = 100
        print("VAR DECLARATION")
        print(self.processingLine)
        startInd = len(SYNTAX_DICTIONARY["var"]) + 1
        self.processingLine = self.processingLine[startInd:len(self.currentLine)]
        #return self.processingLine[startInd:len(self.currentLine)]
        
    def getFunctionDeclaration(self):
        #fudge funcName(blah, blah, blah):
        print("FUNCTION DECLARATION")
        outputStr = "def "
        startInd = len(SYNTAX_DICTIONARY["def"])
        outputStr += self.currentLine[startInd:len(self.currentLine)]
        print(outputStr)
        self.processingLine = outputStr

    def getForDeclaration(self):
        # fur (myhomie i = 0; i < 1; i+=1):
        #fur,(myhomie, i, =, 0;, i, <, 1;, i+=1):
        outputStr = "for "
        outputStr = "i"

    def getEverythingFromCurLineAfterIndex(self, index):
        print()

    def getStringBetweenParantheses(self, instr :str):
        startInd = instr.index("(")
        lastInd = instr.index(")")
        return str[startInd:lastInd+1]
        
        


def main():
    t = Translator(INPUT_FILENAME, OUTPUT_FILENAME)
    t.translate()

    
    print("PROGRAM FINISH")


main()
