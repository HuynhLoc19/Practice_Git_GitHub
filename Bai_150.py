
#   Hãy đưa số 1 về đầu List

from random import *

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(0, 9))
    return lst

def Chuyen_Dau(lst):
    vt = 0
    for i in range(1, len(lst)):
        if lst[i] == 1:
            lst[vt] = lst[vt] + lst[i]
            lst[i] = lst[vt] - lst[i]
            lst[vt] = lst[vt] - lst[i]
            vt += 1
    return lst

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List vừa đc tạo là: ', Tao_Lst(lst, n))
print('List sau khi chuyển 1 lên đầu: ', Chuyen_Dau(lst))

