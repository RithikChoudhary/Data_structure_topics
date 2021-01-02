# Write a program to reverse an array or string

#     Difficulty Level : Basic
#     Last Updated : 08 Sep, 2020

 

# Given an array (or string), the task is to reverse the array/string.
# Examples : 
 

# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}


# def reverseList(A):
#   print( A[::-1])
     
# # Driver function to test above function 
# A = list(map(int,input().strip().split()))
# print(A) 
# print("Reversed list is") 
# reverseList(A)  

    
def reverseList(A,end,start):
    i = end
    reverseFinal = []
    while i >=start:
        reverseFinal.append(A[i])
        i-=1
    print(reverseFinal)
    
if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8]
    end = len(A)-1
    start = 0
     
    reverseList(A,end,start)
    
    