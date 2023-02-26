testcases = int(input())
for tc in range(testcases):
    ar = list(map(int, input().split()))
    # sunny = ar.count(1)
    # rainy = ar.count(0)
    if (ar.count(1)) > (ar.count(0)):
        print("YES")
    else:
        print("NO")