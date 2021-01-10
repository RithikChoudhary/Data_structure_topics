
# Kadane's Algorithm
# Medium Accuracy: 51.0% Submissions: 36157 Points: 4

# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.


def kadane(list1,n):
    
    firstmax = list1[0]
    lastmax = firstmax
    for i in range(len(list1)):
        if i !=0:
            firstmax = max(list1[i],firstmax+list1[i])
            lastmax = max(firstmax,lastmax)
    return lastmax

if __name__ == '__main__':
    
    n = int(input())
    list1 = list(map(int,input().strip().split()))[0:n]
        
    print(kadane(list1,n))
     