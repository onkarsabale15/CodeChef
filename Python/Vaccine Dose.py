# cook your dish here
testcase = int(input())
for tst in range(testcase):
    D,L,R = map(int, input().split())
    if L<=D<=R:
        print("Take second dose now")
    elif D<L:
        print("Too Early")
    else:
        print("Too Late")