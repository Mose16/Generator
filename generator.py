"""
Created by Moses Wescombe. Feel free to change anything you need. Common controls are at the top before Fuctions section.

"""

###Control panel###
#File name
file = open("python.txt", "r")

#Switches:
xPass = True # function(red) -> function(Passing parameters: red)
xAnd = True # "No, yes, plant and kill"
xQuotes = False # "String" -> String
xFuncCheck = True # function() -> call function 'function'

#Add words to replace
PSEUDO = {
    "def ":"Define a function called ",
    "class ":"Define a class called ",
    " = ":"Set variable '",
    "pass ":"Do nothing ",
    "def __init__":"Define object constructor function",
    "==":" is equal to ",
    "<":" is less than ",
    ">":" is greater than ",
    "<=":" is less than or equal to ",
    ">=":" is greater than or equal to ",
    "!=":" is not equal to ",    
}

#Dont forget to add the key to this list
WORDS = [
    "def __init__",
    "def ",
    "class ",
    " = ",
    "pass ",
    "==",
    "<=",
    ">=",
    "!=",
    ">",
    "<"    
]


###---Functions---###
#File managers
def readFileLines(file):
    lines = file.readlines()
    return lines     
    
def createFile(fileName, text):
    newFile = open(fileName + ".txt", "w+")
    newFile.write(text)
    return


#File editors
def functionCheck(line):
    global classSkip
    if line.find("def ") == -1:
        for function in functions:
            if line.find("to " + function + "(") != -1:
                pos = line.find(function + "(")
                line = line[:pos] + "the return of function " + line[pos:]                
            elif line.find(function + "(") != -1 and line.find("called " + function + "(") == -1:
                pos = line.find(function + "(")
                line = line[:pos] + "Call function " + line[pos:]
                        
    if line.find("class ") == -1:
        for class_ in classes:
            if line.find("to " + class_ + "(") != -1:
                pos = line.find(class_ + "(")
                line = line[:pos] + "an iteration of class " + line[pos:]                
            elif line.find(class_ + "(") != -1:
                pos = line.find(class_ + "(")
                line = line[:pos] + "an iteration of class " + line[pos:]    
                         
    return line

def addPass(line):
    if line.find("def ") != -1:
        pass
    elif line.find("class ") != -1:
        pass
    else:
        return line
    
    if line.find("()") == -1:
        if line.find("(") != -1:
            pos = line.find("(") + 1
            line = line[:pos] + "Passing parameters: " + line[pos:]
    return line 

def repAnd(line):
    if line.find(", ") != -1:
        pos = line.rfind(", ")
        line = line[:pos] + " and" + line[pos + 1:]
    return line

def removeQuotes(line):
    progress = 0
    while line[progress:].find("\"") != -1:
        pos = line.find("\"", progress)
        line = line[:pos] + line[pos + 1:]
        progress = pos  
    return line
              
def wordRep(line):
    for word in WORDS:
        if word[:3] == " = ":
            if line.find(word) != -1:
                pos = line.find(word)
                spaces = len(line) - len(line.lstrip())
                line = (" " * spaces) + line[:spaces] + PSEUDO[word] + line[spaces:pos] + "' to " + line[pos + len(word):]
        elif word == "def " or word == "class " or word == "def __init__":
            if line.find(word) != -1:
                ###Add to arrays###
                if word == "class ":
                    classes.append(line[6: min(line.find("(") if not line.find("(") == -1 else 999, line.find(":") if not line.find(":") == -1 else 999)])
                    classes[-1] = classes[-1].strip()
                if word == "def ":
                    functions.append(line[4: min(line.find("(") if not line.find("(") == -1 else 999, line.find(":") if not line.find(":") == -1 else 999)])   
                    functions[-1] = functions[-1].strip()
                
                ###Replace words###                
                pos = line.find(word)
                line = line[:pos] + PSEUDO[word] + line[pos + len(word):]
                
                while line.find(" = ") != -1:
                    pos = line.find(" = ")
                    start = line.rfind(", ", 0, pos)
                    if line.find(", ", pos) != -1:
                        end = line.find(", ", pos)
                    else:
                        end = line.find("):", pos)
                    line =  line[:start + 2] + "(Set parameter '" + line[start + 2:pos] + "' to " + line[pos + 3:end] + " by default)" + line[end:]
        else:
            if line.find(word) != -1:
                pos = line.find(word)
                line = line[:pos] + PSEUDO[word] + line[pos + len(word):]                

    return line
        
            
        

###---Variables---###
functions = []
classes = []





###-------Main Code-------###
lines = readFileLines(file)
newFile = ""
for line in lines:  
    #Conditionals
    if xPass:
        line = addPass(line)
    line = wordRep(line)
    if xAnd:
        line = repAnd(line)
    if xQuotes:
        line = removeQuotes(line)
        
    newFile += line
    
createFile("generatedFile", newFile)
lines = readFileLines(open("generatedFile.txt", "r"))
newFile = ""

if xFuncCheck:
    for line in lines:
        line = functionCheck(line)    
        if xPass:
            line = addPass(line)  
        newFile += line
    
createFile("generatedFile", newFile)
    

print(newFile)
print(classes, functions)



