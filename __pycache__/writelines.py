outFile = None
outStr = ""

outFile = open("C:\AICLASS\함수예제.txt.txt", "w")

outStr = "안녕하세요?"
outFile.writelines(outStr+"\n")

outStr = "반갑습니다"
outFile.writelines(outStr+"\n")

outStr = "자주 만나요 ^^"
outFile.writelines(outStr+"\n")

outFile.close()
print("---AICLASS.txt 파일이 저장됨---")