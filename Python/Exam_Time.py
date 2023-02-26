T = int(input())
for i in range(T):
    mar = []
    for j in range(2):
        arr = list(map(int, input().split()))
        mar.append(arr)

    Sloth = mar[1]

    if sum(mar[0])==sum(mar[1]):
        if mar[0][0]==mar[1][0]:
            if mar[0][1]==mar[1][1]:
                if mar[0][2]==mar[1][2]:
                    print("TIE")
                else:
                    if mar[0][2]>mar[1][2]:
                        print("Dragon")
                    else:
                        print("Sloth")
            else:
                if mar[0][1]>mar[1][1]:
                    print("Dragon")
                else:
                    print("Sloth")
        else:
            if mar[0][0]>mar[1][0]:
                print["Dragon"]
            else:
                print("Sloth")
    elif sum(mar[0])>sum(mar[1]):
        print("Dragon")
    else:
        print("Sloth")