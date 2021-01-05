def sort012(arr,n):
    low=0
    high=n-1
    
    mid=0
    while mid<=high:
        if arr[mid]==0:
            arr[mid] , arr[low] = arr[low] , arr[mid]
            mid+=1
            low+=1
        
        elif arr[mid]==1:
            mid+=1
        
        else:
            arr[mid] , arr[high] = arr[high] , arr[mid]
            high-=1
    return arr

    

