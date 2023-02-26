# cook your dish here
testcase = int(input())
for tst in range(testcase):
    N,A,B,C = map(int, input().split())
    if (A+C)>=B and B>=N:
        print("YES")
    elif N<=(A+C)<=B:
        print("YES")
    else:
        print("NO")