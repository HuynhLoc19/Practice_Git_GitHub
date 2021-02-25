
#   Kiểm tra LIST có tồn tại hai giá trị không liên tiếp hay ko

from random import *

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(0, 20))
    return lst

def Check_Continous(lst):
    flag = 1
    for i in range(n-1):
        if(lst[i+1]-lst[i] != 1):
            return 0

def K_Tra(lst):
    print('List tồn tại hai giá trị không liên tiếp nhau. ') if Check_Continous(lst) == 0 else print('List liên tiếp nhau. ')

lst = []
n = int(input('Nhập số lượng phần tử của Lst: '))
print('List được tạo là: ', Tao_Lst(lst, n))
K_Tra(lst)