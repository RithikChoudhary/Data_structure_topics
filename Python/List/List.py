nums = [23,4,1,123,4]
print(nums[0])

# after index value 2 it will print all 

print(nums[2:])
# it can take any value 
nums2 = [9.5,'rithik',5]
print(nums2)

# we can make list in list 
mil = [nums,nums2]
# print(mil)


# we can use insert,pop,del,remove(it take element) and all other take index value 
nums.insert(2,15)
print(nums)
nums.pop(1)
print(nums)

print(min(nums))
print(max(nums))
print(nums.sort())
del nums2[2:]
print(nums2)

print(sum(nums))