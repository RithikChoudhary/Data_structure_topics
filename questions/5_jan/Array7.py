def rotate(list1):
    num = list1[len(list1)-1]
    
    for i in range(len(list1)-1,-1,-1):
        list1[i]= list1[i-1]
    
    list1[0] = num
    return list1
   
   
        
if __name__ == '__main__':
    test = int(input())
    see = []
    while test > 0:
        x = input()
        list1 = list(map(int,input().strip().split()))
        z = rotate(list1)
        see.append(z)
        test-=1
    for j in (see):
        print(*j)
    
    
    
      
    