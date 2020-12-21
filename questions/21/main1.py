# write a program to print the nth term of the series :

# 1, 76, 38, 19, 45, 9, 21, 7, 3 55, 321, 40000, 679878933, 1232998540, 1, 76, 38, 19...
# Note : The series repeats itself after 14 terms.
# ex
# input :
# Enter Pos : 5
# output : 
# 45


def cal(input):
    num = [1,2,4,7,3,1,2,4,7,9]
    
    if input <= len(num):
        return num[input-1]
    else:    
        for i in num:
            pos = input-len(num)
            if pos <= len(num):
                return num[pos-1]
                break    
            input = pos
            
if __name__ == '__main__':
    input = int(input("Enter pos = "))
    print(cal(input))
    




















# elif input != index:
#             for i in range(input):
#                 length = input-len(num)
#                 if len(num) > length:
#                     return (num[length])
#                     break
#         else:
#             pass




# for index,val in enumerate(num):
    #     if input == index:
    #         return (val)
    #     else:
    #         for i in range(input):
    #             if input > len(num)-1:
    #                 getin = input-len(num)-1
    #                 if input <= len(num)-1 or (input == len(num)-1):
    #                     return num[getin]