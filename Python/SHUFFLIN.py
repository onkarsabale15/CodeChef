import math
testcases = int(input())
for tc in range(testcases):
    N = int(input())
    ar = list(map(int, input().split()))
    #Counting Numbers of even and odd terms
    count_odd = 0
    count_even = 0
    for num in ar:
        if num%2:
            count_odd += 1
        else:
            count_even += 1
    num_odd = math.ceil(N/2)
    num_even = math.floor(N/2)
    maximum_value = min(count_odd,num_even) + min(count_even, num_odd)
    print(maximum_value)