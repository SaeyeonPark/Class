outFile = None
outStr = ""

outFile = open("C:\AICLASS\함수예제.txt.txt", "w")

while True :
    outStr = input("내용 입력 ==> ")
    if outStr != "" :
        outFile.writelines(outStr+"/n")
    else :
        break

outFile.close()
print("---AICLASS 파일이 저장됨---")