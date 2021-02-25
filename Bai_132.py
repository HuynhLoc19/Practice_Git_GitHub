
 #  Hãy tạo List B từ các số lẻ của List A

from random import randrange

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(0, 20))
    return lst 

def Mang_Le(lst):
    C = []
    for elem in lst:
        if elem % 2 != 0:
            C.append(elem)
    return C

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List vừa đc tạo là: ', Tao_Lst(lst, n))
print('List các số lẻ từ List A là: ', Mang_Le(lst))