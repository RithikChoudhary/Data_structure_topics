# iterate two list at one time 


fruits = ['apple','orange','banana','mango']
nums = [1,2,3,4,5,6]

# zip make list of every index elements 
z = zip(fruits,nums)

for fruit,nums in z:
    print('apple' in fruit)

# print('apple' in z)
