# Selection sort algo

def selectionsort(arr):
    for i in range(len(arr)):
        mid =i
        for j in range(i+1,len(arr)):
            if arr[mid] > arr[j]:
                mid = j
        temp =  arr[mid]
        arr[mid] = arr[i]
        arr[i] = temp
        print(arr)



if __name__ == '__main__':
    arr = list(map(int,input().strip().split()))
    selectionsort(arr)
    