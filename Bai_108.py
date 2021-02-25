
#   Viết hàm tìm UCLN của tất cả các phần tử trong List

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

# HÀm tìm UCLN của tất cả các phàn tử trong  List
def UCLN(a, b):
    a = abs(a)
    b = abs(b)
    while a*b != 0:
        if a > b:
            a = a-b
        else:
            b = b - a
    return a+b

# Hàm tính UCLN của tất cả các phần tử trong LIst
def UC_List(lst):
    lc = lst[0]
    for elem in lst:
        lc = UCLN(lc, elem)
    return lc

lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
print('Ước chung lớn nhất của tất cả các phần tử trong List là: ', UC_List(lst))