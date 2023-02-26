T = int(input())
for _ in range(T):
    N, Q = map(int, input().split())
    arrr = []
    Que = []
    for x in range(N):
        arrr.append(list(map(int, input().split())))
    
    for y in range(Q):
        Que.append(list(map(int, input().split())))
    gold = []
    silver = []
    bronze = []
    for z in range(N):
        lis = arrr[z]
        gold.append(lis[0])
        silver.append(lis[1])
        bronze.append(lis[2])
    g_max = max(gold)
    s_max = max(silver)
    b_max = max(bronze)
    for w in range(Q):
        k = Que[w]
        j = k[0] - 1
        if g_max>gold[j]:
            g_diff = g_max - gold[j]
            to_add_g = g_diff + 1
            add_g = gold[j] + to_add_g
            print(to_add_g)
        elif s_max>silver[j]:
            s_diff = s_max - silver[j]
            to_add_s = s_diff + 1
            add_s = silver[j] + to_add_s
            print(to_add_s)
        elif b_max>bronze[j]:
            b_diff = b_max - bronze[j]
            to_add_b = b_diff + 1
            add_b = bronze[j] + to_add_b
            print(bronze[j])
        else:
            print(1)