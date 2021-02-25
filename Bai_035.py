
#   Tính tổng các giá trị có chữ số hàng chục là số 5 trrong list

from random import *

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(150, 360))
    return lst

def Tao_Hai(lst):
    for i in range(len(lst)):
        Str = str(lst[i])
        if Str[len(Str)-2] == '5':
            print(lst[i], end=' ')

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List vừa đc tạo là: ', Tao_List(lst, n))
Tao_Hai(lst)