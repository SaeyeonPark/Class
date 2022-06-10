from cmath import inf


inFile = None
inStr = ""

inFile = open ("C:/AICLASS.txt", "r", encoding="UTF-8")

inStr = inFile.readline()
print(inStr, end="")

inStr = inFile.readline()
print(inStr, end="")

inStr = inFile.readline()
print(inStr, end="")

inFile.close()