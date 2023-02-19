from env import *

class Translator:
    def __init__(self, inputFileName :str, outputFileName :str):
        self.file = open(inputFileName, "r")
        self.outputFile = open(outputFileName, "w+")

        self.currentLine = ""
        self.lineToAddAtEndOfBlock = ""

        self.tabNum = 0

    
    def translate(self):
        for line in self.file:
            if line == "\n":
                continue #TODO - Try to get rid of this

            self.currentLine = line
            modifiedLine = line
            prevTabNum = self.tabNum
            if self.setTabNum() < prevTabNum:
                self.writeStatementToEndOfBlock()
                self.lineToAddAtEndOfBlock = ""

            modifiedLine = self.removeNewline(modifiedLine)
            modifiedLine = self.removeTab(modifiedLine)
            modifiedLine = self.determineWhichStatement(modifiedLine)
            self.writeToFile(modifiedLine)

        if self.lineToAddAtEndOfBlock != "":
            self.writeToFile(self.lineToAddAtEndOfBlock)
    
    def determineWhichStatement(self, line):
        # bunch of different if statements
        print(line)
        currentWordList = line.split()
        print(currentWordList)
        line = line.replace(SYNTAX_DICTIONARY["print"], "print")
        line = line.replace(SYNTAX_DICTIONARY["input"], "input")
        line = line.replace("++", " += 1")
        line = line.replace("--", " -= 1")

        firstWord = currentWordList[0].lower()
        if firstWord == SYNTAX_DICTIONARY["var"]:
            line = self.getVarDeclaration(line)
        elif firstWord == SYNTAX_DICTIONARY["def"]:
            line = self.setDefDeclaration(line)
        elif firstWord == SYNTAX_DICTIONARY["while"]:
            line = self.getWhileDeclaration(line)
        elif firstWord == SYNTAX_DICTIONARY["for"]:
            line = self.getForDeclaration(line)
        elif firstWord == SYNTAX_DICTIONARY["if"]:
            line = self.getIfDeclaration(line)
        elif SYNTAX_DICTIONARY["else"] in firstWord:
            line = self.getElseDeclaration(line)

        return line
        

    def removeNewline(self, line :str):
        if line[-1] == '\n':
            return line[0:-1]
        else:
            return line

    #-------------Tabs
    def setTabNum(self):
        count = 0
        while self.currentLine[count] == " ":
            count += 1
        self.tabNum = count
        return count

    # setTabNum need to be run before removeTab can work properly
    def removeTab(self, line):
        return line[self.tabNum:]

    def getTabStr(self):
        mystr = ""
        for i in range(self.tabNum):
            mystr += " "
        return mystr

    def writeStatementToEndOfBlock(self):
        lineToWrite = "    " + self.lineToAddAtEndOfBlock + '\n'
        self.writeToFile(lineToWrite)

    def writeToFile(self, processedLine :str):
        processedLine = self.getTabStr() + processedLine + '\n'
        print("WRITING STR: " + processedLine)
        self.outputFile.write(processedLine)
        

    #---------Conversion

    def getVarDeclaration(self, line :str):
        # myHomie i = 100
        startInd = len(SYNTAX_DICTIONARY["var"]) + 1
        return line[startInd:len(self.currentLine)]
        
    def getDefDeclaration(self, line :str):
        #fudge funcName(blah, blah, blah):
        outputStr = "def "
        startInd = len(SYNTAX_DICTIONARY["def"])
        outputStr += self.currentLine[startInd:len(self.currentLine)]
        return outputStr

    def getWhileDeclaration(self, line :str):
        return line.replace("keepgoing", "while").replace("(", "").replace(")", "")



    def getForDeclaration(self, forloopline :str):
        # Change to while loop
        # fur (myhomie i = 0; i < 1; i+=1):
        #fur,(myhomie, i, =, 0;, i, <, 1;, i+=1):
        print("FOR LOOP: ------------------" + forloopline)
        mystr = self.determineWhichStatement(self.getForLoopInitStr(forloopline))
        self.writeToFile(mystr)

        self.lineToAddAtEndOfBlock = self.getForLoopUpdateStr(forloopline)
        return "while " + self.getForLoopConditionStr(forloopline) + ":"


        
    def getForLoopInitStr(self, forLoopStmt :str) -> str:
        startInd = forLoopStmt.index("(")
        lastInd = forLoopStmt.index(';')
        return forLoopStmt[startInd+1:lastInd]

    def getForLoopConditionStr(self, forLoopStmt :str) -> str:
        startInd = forLoopStmt.index(";") + 1
        while forLoopStmt[startInd] == " ":
            startInd += 1
        lastInd = startInd + forLoopStmt[startInd+1:].index(';') #Find second ;
        return forLoopStmt[startInd:lastInd+1]

    def getForLoopUpdateStr(self, forLoopStmt :str) -> str:
        initSemi = forLoopStmt.index(';') + 1
        startInd = initSemi + forLoopStmt[initSemi:].index(';') + 1
        while forLoopStmt[startInd] == " ":
            startInd += 1
        lastInd = forLoopStmt.index(')')
        return forLoopStmt[startInd:lastInd]

    def getIfDeclaration(self, ifLine :str):
        return ifLine.replace("this", "if").replace("(", "").replace(")","")

    def getElseDeclaration(self, elseLine :str):
        return elseLine.replace("that", "else")




    def getStringBetweenParantheses(self, instr :str):
        startInd = instr.index("(")
        lastInd = instr.index(")")
        return str[startInd:lastInd+1]
        
        



def main():
    t = Translator(INPUT_FILENAME, OUTPUT_FILENAME)
    t.translate()
    print("PROGRAM FINISH")

main()
