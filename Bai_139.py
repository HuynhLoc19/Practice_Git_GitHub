
#   Sắp xếp các giá trị tại các VỊ TRÍ lẻ trong LIST các số nguyên tăng dần, các giá trị khác giữ nguyên giá trị và vị trí

from random import *

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(0, 20))
    return lst

def Xep_Le(lst, n):
    for i in range(1, n, 2):
        for j in range(i+2, n, 2):
            if lst[j] < lst[i]:
                lst[i] = lst[i] + lst[j]
                lst[j] = lst[i] - lst[j]
                lst[i] = lst[i] - lst[j]

    return lst

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List vừa đc tạo là: ', Tao_Lst(lst, n))
print('List sau khi sắp xếp các số tại các vị trí lẻ tăng dần là: ', Xep_Le(lst, n))