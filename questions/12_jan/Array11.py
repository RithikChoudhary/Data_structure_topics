# Find the Duplicate Number
# Medium

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2



def finddup(nums):
    count = 0
    a = None
    for i in nums:
        for j in nums:
            if i == j:
                count+=1
                if count > 1:
                    a=i
                    break
        count=0
    print(a)




if __name__ == '__main__':
    nums = list(map(int,input().strip().split()))
    finddup(nums)
    
    # [1,3,4,2,2]