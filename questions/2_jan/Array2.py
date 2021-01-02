# Maximum and minimum of an array using minimum number of comparisons

def comparision(A):
    min = 0
    max = 1
    minmax = [None, None]          
    if (len(A)-1)  == 1:
        minmax[min] = A[0]
        minmax[max] = A[0]
        return minmax
        
    if A[0] < A[1]:
        minmax[min] = A[0]
        minmax[max] = A[1]
    else:
        minmax[min] = A[1]
        minmax[max] = A[0]
        
    for i in A[1:]:
        if A[i] > minmax[max]:
            minmax[max] = A[i]
        elif A[i] < minmax[min]:
            minmax[min] = A[i]
        else:
            pass
    return minmax

if __name__ == '__main__':
    A = [100,2200,3,2,1,200,4,666]
    print(comparision(A))
    
    
    