INPUT_FILENAME = "inputCode.txt"
OUTPUT_FILENAME = "output.py"

SYNTAX_DICTIONARY = {
    "var" : "myhomie",
    "def" : "fudge",
    "for" : "fur",
    "print" : "gundam",
    "input" : "whatDoYouWant",
    "while" : "keepgoing"
}


class Translator:
    def __init__(self, inputFileName :str, outputFileName :str):
        self.file = open(inputFileName, "r")
        self.outputFile = open(outputFileName, "w+")

        self.currentLine = ""
        self.processingLine = ""
        self.currentWordList = ""
        self.lineToAddAtEndOfBlock = ""

        self.tab = 0
        

    def removeNewlineFromProcessedLine(self):
        if self.processingLine[len(self.processingLine)-1] == '\n':
            self.processingLine = self.processingLine[0:len(self.processingLine)-1]

    def removeTabFromProcessedLine(self):
        self.setTabNum()
        self.processingLine = self.processingLine[self.tab:len(self.processingLine)]

    def getTab(self):
        return self.currentLine[0:self.tab]

    def setTabNum(self):
        count = 0
        while self.currentLine[count] == " ":
            count += 1
        
        self.tab = count
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
            self.removeTabFromProcessedLine()
            self.currentWordList = self.currentLine.split()
            self.determineWhichStatement()


            self.writeToFile()

            

    def writeToFile(self):
        self.processingLine = self.getTab() + self.processingLine + '\n'
        print("WRITING STR: " + self.processingLine)
        self.outputFile.write(self.processingLine)
        

    def determineWhichStatement(self):
        # bunch of different if statements
        print(self.processingLine)
        self.currentWordList = self.processingLine.split()
        if SYNTAX_DICTIONARY["print"] in self.processingLine:
            self.processingLine = self.processingLine.replace(SYNTAX_DICTIONARY["print"], "print")

        if SYNTAX_DICTIONARY["input"] in self.processingLine:
            self.processingLine = self.processingLine.replace(SYNTAX_DICTIONARY["input"], "input")

        if "++" in self.processingLine:
            self.processingLine = self.processingLine.replace("++", "+= 1")
        
        if "--" in self.processingLine:
            self.processingLine = self.processingLine.replace("--", "-= 1")


        firstWord = self.currentWordList[0].lower()
        if firstWord == SYNTAX_DICTIONARY["var"]:
            self.setVarDeclaration()
        elif firstWord == SYNTAX_DICTIONARY["def"]:
            self.setDefDeclaration()
        elif firstWord == SYNTAX_DICTIONARY["while"]:
            self.setWhileDeclaration()
        elif firstWord == SYNTAX_DICTIONARY["for"]:
            self.setForDeclaration()


    def setVarDeclaration(self):
        # myHomie i = 100
        startInd = len(SYNTAX_DICTIONARY["var"]) + 1
        self.processingLine = self.processingLine[startInd:len(self.currentLine)]
        #return self.processingLine[startInd:len(self.currentLine)]
        
    def setDefDeclaration(self):
        #fudge funcName(blah, blah, blah):
        outputStr = "def "
        startInd = len(SYNTAX_DICTIONARY["def"])
        outputStr += self.currentLine[startInd:len(self.currentLine)]
        self.processingLine = outputStr

    def setWhileDeclaration(self):
        self.processingLine.replace("(", "")
        self.processingLine.replace(")", "")

    def setForDeclaration(self):
        # fur (myhomie i = 0; i < 1; i+=1):
        #fur,(myhomie, i, =, 0;, i, <, 1;, i+=1):
        print("FOR LOOP: ------------------" + self.processingLine)
        # eval initialization

        tmp = self.processingLine
        print(self.getForLoopInitStr())
        print(self.getForLoopConditionStr())
        print(self.getForLoopUpdateStr())


        self.processingLine = self.getForLoopInitStr()
        self.determineWhichStatement()
        self.writeToFile()

        self.processingLine = tmp
        self.processingLine = "while " + self.getForLoopConditionStr() + ":"
        self.writeToFile()

        self.processingLine = tmp
        self.processingLine = "    " + self.getForLoopUpdateStr() #TODO - Hardcoded 
        #self.writeToFile() #TODO - Need to add update statement at the end of the while loop

        #self.processingLine = ""
        
        
        




        
    def getForLoopInitStr(self) -> str:
        startInd = self.processingLine.index("(")
        lastInd = self.processingLine.index(';')
        return self.processingLine[startInd+1:lastInd]

    def getForLoopConditionStr(self) -> str:
        startInd = self.processingLine.index(";") + 1
        while self.processingLine[startInd] == " ":
            startInd += 1
        lastInd = startInd + self.processingLine[startInd+1:len(self.processingLine)].index(';') #Find second ;
        return self.processingLine[startInd:lastInd+1]

    def getForLoopUpdateStr(self) -> str:
        initSemi = self.processingLine.index(';') + 1
        #print(self.processingLine[initSemi:])
        startInd = initSemi + self.processingLine[initSemi:].index(';') + 1
        while self.processingLine[startInd] == " ":
            startInd += 1
        lastInd = self.processingLine.index(')')
        return self.processingLine[startInd:lastInd]

        # fur (myhomie i = 0; i < 1; i+=1):
        # init = 18; expected startInd = 25



    def getStringBetweenParantheses(self, instr :str):
        startInd = instr.index("(")
        lastInd = instr.index(")")
        return str[startInd:lastInd+1]
        
        




def main():
    t = Translator(INPUT_FILENAME, OUTPUT_FILENAME)
    t.translate()

    
    print("PROGRAM FINISH")


main()
