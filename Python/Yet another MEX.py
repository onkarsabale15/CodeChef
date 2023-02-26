testcase = int(input())
for i in range(testcase):
    N,K = map(int, input().split())
    arr = list(map(int, input().split()))
    B = list(range(N+1))
    mex = []
    for i in range(len(B)):
        for j in range(len(arr)):
            if B[i]!=arr[j]:
                mex.append(B[i])
                j += 1
            else:
                j += 1
        i += 1
    set_mex = set(mex)
    set_b = set(B)
    semi_fin = set_mex & set_b
    final = list(set_b-semi_fin)
    print(final)