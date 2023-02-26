# cook your dish here
testcase = int(input())
for tst in range(testcase):
    A,B,C,D,E = map(int, input().split())
    if (A+B <= D and C<=E)or(B+C <= D and A<=E)or(C+A <= D and B<=E):
        print("YES")
    else:
        print("NO")