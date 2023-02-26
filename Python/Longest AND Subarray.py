for t in range(int(input())):
    n = int(input())
    a, b, l = list(range(1, n + 1)), [1], 1
    for i in range(n):
        if n == 1:
            break
        elif a[i] & a[i - 1] > 0:
            l += 1
        else:
            if b[0]<l:
                b[0] = l
            l = 1
    if b[0]<l:
        b[0]=l
    print(b[0])