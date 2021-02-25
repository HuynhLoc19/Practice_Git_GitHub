
#   Sắp xếp các số dương tong List các số thực tăng dần còn các số âm giữ nguyên ị trí của chúng trong List

from random import *

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(round(uniform(-10, 20), 2))
    return lst

def Xep_Duong(lst, n):
    for elem in lst:
        for i_elem in lst:
            if elem>0 and i_elem>0 and elem>i_elem:
                elem = elem + i_elem
                i_elem = elem - i_elem
                elem = elem - i_elem
    return lst

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List vừa đc tạo là: ', Tao_Lst(lst, n))
print('List sau khi sắp xếp các số tại các số dương tăng dần là: ', Xep_Duong(lst, n))