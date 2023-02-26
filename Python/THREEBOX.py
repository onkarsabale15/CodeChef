testcase = int(input())
for tst in range(testcase):
    A,B,C,D = map(int, input().split())
    if (A+B+C)<=D:
        print("1")
    elif (A+B<=D and C<=D) or (B+C<=D and A<=D) or (A+C<=D and B<=D):
        print("2")
    elif 0 < A <= D and 0 < B <= D and 0 < C <= D:
        print("3")