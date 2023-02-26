# Question at :- https://www.codechef.com/SEPT21C/problems/TRAVELPS


#testcase as per input format
testcase = int(input("No Of Testcase = "))


#To take input number of inputs given in testcase
for tst in range(testcase):

    #to take evenly spaced input of N A B
    N,A,B = map(int, input("N A B = ").split())


    #To take binary inputs
    string = input("Values of N = ")

    #To count no of district passes
    dist_pass = string.count('0')

    #To count no of state passes
    state_pass = string.count('1')

    print("Time Spent on Filling Form =",dist_pass*A + state_pass*B)