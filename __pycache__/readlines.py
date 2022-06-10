inFile = None
inList = []

inFile = open("C:\AICLASS\함수예제.txt.txt", "r", encoding="UTF-8")

inList = inFile.readlines()
print(inList)

inFile.close()