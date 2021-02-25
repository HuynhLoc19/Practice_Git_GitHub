
#   Tìm chữ số xuất hiện ít nhất trong List

from random import *

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

def Vi_Tri_min(C):
    m = 0
    for i in range(len(C)):
        if C[i] < C[m]:
            m = i
    return m

def Xuat_Hien(lst):
    C = [0]*10
    for elem in lst:
        if elem == 0:
            C[0] += 1
        t = elem
        while t != 0:
            dv = t%10
            C[dv] += 1
            t //= 10
    return Vi_Tri_min(C)


lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List sau khi tạo là: ', Tao_Lst(lst, n))
print('Chữ số xuất hiện ít nhất trong Lst là: ', Xuat_Hien(lst))
