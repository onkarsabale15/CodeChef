# cook your dish here
testcase = int(input())
for tst in range(testcase):
    N,P,X,Y = map(int, input().split())
    binar = list(map(int, input().split()))
    elderly = binar[:P].count(1)
    child = binar[:P].count(0)
    time = (elderly*Y) + (child*X)
    print(time)