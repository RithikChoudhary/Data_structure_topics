# write a program to print the nth term of the series :

# 1, 76, 38, 19, 45, 9, 21, 7, 3 55, 321, 40000, 679878933, 1232998540, 1, 76, 38, 19...
# Note : The series repeats itself after 14 terms.
# ex
# input :
# Enter Pos : 5
# output : 
# 45


def cal(enter):
    num = [1,2,4,7,3,1,2,4,7,9]
    
    if enter <= len(num):
        return num[enter-1]
    else:    
        for i in num:
            ind = enter-len(num)
            if ind <= len(num):
                return num[ind-1]
                break    
            enter = ind
            
if __name__ == '__main__':
    enter = int(input("Enter pos = "))
    print(cal(enter))
    




















# elif enter != index:
#             for i in range(enter):
#                 length = enter-len(num)
#                 if len(num) > length:
#                     return (num[length])
#                     break
#         else:
#             pass




# for index,val in enumerate(num):
    #     if enter == index:
    #         return (val)
    #     else:
    #         for i in range(enter):
    #             if enter > len(num)-1:
    #                 getin = enter-len(num)-1
    #                 if enter <= len(num)-1 or (enter == len(num)-1):
    #                     return num[getin]