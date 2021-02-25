
#   Tính tổng các giá trị nhỏ hơn các giá trị xung quanh

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

def Xung_Quanh(lst):
    S = 0
    if lst[0] < lst[1]:
        S += lst[0]
    for i in range(1, len(lst)-1):
        if lst[i]<lst[i+1] and lst[i]<lst[i-1]:
            S += lst[i]
    if lst[len(lst)-1] < lst[len(lst)-2]:
        S += lst[len(lst)-1]
    return S


lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
print('Tổng các giá trị nhỏ hơn các giá trị xung quanh là: ', Xung_Quanh(lst))
