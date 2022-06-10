inFp, outFp = None, None
inStr = ""

inFp = open("C:\AICLASS\함수예제.txt.txt", "r")
outFp = open("C:\AICLASS\Temp.txt", "w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("---파일이 정상적으로 복사되었음---")