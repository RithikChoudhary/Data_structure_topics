def merge(arr1,arr2):
    arr1[:]=sorted(arr1+arr2)
    arr2.clear()
    print(arr1)
        
         


if __name__ == '__main__':
    n,m = map(int,input().strip().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    merge(arr1,arr2)
    