inFile = None
inStr = ""
lineNum = 1

inFile = open("C:\AICLASS\함수예제.txt.txt", "r", encoding="UTF-8")

while True :
    inStr = inFile.readline()
    if inStr == "" :
        break
    print(lineNum, " : ", inStr, end="")
    lineNum += 1

inFile.close()