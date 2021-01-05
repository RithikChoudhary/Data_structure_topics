def union(list1,list2):
    list1 = list1+list2
    listFinal = []
    for i in list1:
        if i not in listFinal:
            listFinal.append(i)
    return (len(listFinal))
        

if __name__ == '__main__':
    test = int(input())
    see = []
    while test > 0:
        x,y = input().split()
        list1 = list(map(int,input().strip().split()))
        list2 = list(map(int,input().strip().split()))
        z = union(list1,list2)
        see.append(z)
        test-=1
    for j in see:
        print(j)