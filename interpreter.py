
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
    "print" : "whatDoYouWant"
}


class Translator:
    def __init__(self, inputFileName :str, outputFileName :str):
        self.file = open(inputFileName, "r")
        self.outputFile = open(outputFileName, "w+")
        self.currentLine = ""
        self.currentWordList = ""

    def removeNewlineFromCurrentLine(self):
        if self.currentLine[len(self.currentLine)-1] == '\n':
            self.currentLine = self.currentLine[0:len(self.currentLine)-1]

    def translate(self):
        print("okay")
        # for every line:
            # use first word in line as key to which func to translate

        for line in self.file:
            if line == "\n":
                continue #TODO - Try to get rid of this

            self.currentLine = line
            self.removeNewlineFromCurrentLine()
            print("INPUT: " + self.currentLine)
            self.currentWordList = self.currentLine.split()

            outputStr = self.getTab()
            outputStr += self.determineWhichStatement()
            print("WRITING STR: " + outputStr)

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

        if SYNTAX_DICTIONARY["print"] in self.currentLine:
            return self.currentLine.replace(SYNTAX_DICTIONARY["print"], "print")
        
        return "ERROR - NO SYNTAX MATCHED"

    def getVarDeclaration(self):
        # myHomie i = 100
        print("VAR DECLARATION")
        return f"{self.currentWordList[1]} = {self.currentWordList[3]}"
        
    def getFunctionDeclaration(self):
        #fudge funcName(blah, blah, blah):
        print("FUNCTION DECLARATION")
        outputStr = "def "
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

    def getStringBetweenParantheses(self, instr :str):
        startInd = instr.index("(")
        lastInd = instr.index(")")
        return str[startInd:lastInd+1]
        
        


def main():
    t = Translator(INPUT_FILENAME, OUTPUT_FILENAME)
    t.translate()
    import output
    
    print("PROGRAM FINISH")


main()
