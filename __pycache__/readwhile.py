from msilib.schema import IniFile


IniFile = None
inStr = ""

inFile = open ("C:\AICLASS\함수예제.txt.txt", "r", encoding="UTF-8")

while True :
    inStr = inFile.readline()
    if inStr == "" :
        break
    print(inStr, end='')

inFile.close()