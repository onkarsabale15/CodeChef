testcase = int(input())
for tst in range(testcase):
    N = int(input())
    B = 2
    A = B + N
    while A-B != N:
        A +=1
        B +=1
    print(A,B)