# cook your dish here
for tst in range(int(input())):
    N, arr, b, length = int(input()), list(range(1,N+1)), [1], 1
    for i in range(N):
        if N == 1:
            break
        elif arr[i]&arr[i-1] >0:
            length,i = length+1, i+1
        else:
            b.append(length)
            length, i = 1, i+1
    b.append(length)
    print(max(b))