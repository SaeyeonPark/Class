value = 0
while True:
    print("/n현재 값 : ", value)
    line = input("작업 명령 입력 : ")
    tokens = line.split()
    if len(tokens) > 0 :
        op = tokens[0]
        if len(tokens) == 1 :
            if op == 'x' :
                break
            print("잘못된 작업 명령")
        elif len(tokens) == 2 :
            opd = int(tokens[1])
            if op == '=' :
                value = opd
            elif op == '+' :
                value += opd
            elif op == '-' :
                value -= opd
            elif op == '*' :
                value *= opd
            elif op == '/' or op == '%':
                if op != 0:
                    if op == '/' :
                        value /= opd
                    else :
                        value %= opd
                else :
                    print("잘못된 작업 명령(0으로 나누기)")
            else :
                print("잘못된 작업 명령")
        else :
            print("잘못된 작업 명령")