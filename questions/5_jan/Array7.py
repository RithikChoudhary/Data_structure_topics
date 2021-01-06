def rotate(list1):
    zoom=[]
    for i in list1[-1:-5:-4]:
        print(i)
    return (zoom)    
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
    
    
    
      
    