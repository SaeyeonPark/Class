import sys

T = int(sys.stdin.readline())
for t in range(T) :
    add = 0
    even = 0
    a = list(map(int, sys.stdin.readline().split()))

    for i in range(3) :
        if a[i] % 2 == 0 :
            even += 1
        else :
            odd += 1
        
    if(even == 3 or even == 2) :
        print('R')
    else :
        print('B')