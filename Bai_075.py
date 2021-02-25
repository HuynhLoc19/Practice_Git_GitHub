
#   Hãy tìm giá trị trong List xa giá trị x nhất.

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

def Xa_X(lst, x):
    lc = lst[0]
    for elem in lst:
        if abs(elem-x) > abs(lc-x):
            lc = elem
    return lc

lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
x = int(input('Nhập giá trị x: '))
print(f'Giá trị xa {x} nhất trong List là: ', Xa_X(lst, x))