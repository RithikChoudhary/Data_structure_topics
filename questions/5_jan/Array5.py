# Move all negative numbers to beginning and positive to end with constant extra space


def doit(sort):
    start = 0
    for i in range(len(sort)):
        if sort[i] < 0:
            temp = sort[i]
            sort[i] = sort[start]
            sort[start] = temp
            start+=1
    return sort


if __name__ == '__main__':
    sort = list(map(int,input().strip().split()))
    print(doit(sort))
    