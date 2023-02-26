testcase = int(input())
for tst in range(testcase):
    M,N,K = map(int, input().split())
    if (N*K)<M:
        print("YES")
    else:
        print("NO")