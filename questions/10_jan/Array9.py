# minimize the height of towers

class solution:
    def minimize(arr,k,n):
        arr1 = []
        for i in range(n):
            if (arr[i] - k) <=0:
                b = arr[i] + k
                arr1.append(b)
            else:
                c = arr[i] + k
                arr1.append(c)
            return (max(arr1)-min(arr1))
       



if __name__ == '__main__':
    k = input()
    n = input()
    arr = list(map(int,input().strip().split()))[0:n]
    ob = solution()
    print(ob.minimize(arr,k,n))
    
    
    
    
    #  diff = max(arr) - k
    #     arr1 = []
    #     for i in range(n):
    #         b = arr[i] + k
    #         if b < diff:
    #             arr1.append(b)
    #         else:
    #             c = arr[i] - k
    #             arr1.append(c) 
                
    #     return arr1