# Write a Python program to remove duplicates from a list.


nums = [2,4,6,2,3,5,7,4,2]
print(set(nums))

# ////////////////////////////////
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)