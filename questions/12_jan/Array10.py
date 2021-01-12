# # 
# Minimum number of jumps
# Medium Accuracy: 32.96% Submissions: 21680 Points: 4

# Given an array of integers where each element represents the max number of steps that can be made forward from that element. 
# Find the minimum number of jumps to reach the end of the array (starting from the first element). 
# If an element is 0, then you cannot move through that element. 


def jump(arr,n):
    j = 0
    count  = 0
    while j < n:
         j = arr[j]+j
         count+=1
         print(j)
    print(count)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    jump(arr,n)
    
    