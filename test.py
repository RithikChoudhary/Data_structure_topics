arr = [1,0,4,6,0,2,3]
arr1=[]
count=0
for i in range(len(arr)):
    if arr[i] == 0:
        count+=1
    else:
        arr1.append(arr[i])
for j in range(count):
    arr1.append(0)
print(arr1)



