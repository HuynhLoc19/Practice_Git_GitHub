
#   Tìm giá trị x sao cho đoạn [-x,x] chứa tất cả các phần tử trong lst

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(-20, 10))
    return lst

def Tim_Max(lst):
    M = lst[0]
    for elem in lst:
        if elem > M:
            M = elem
    return M

def Tim_min(lst):
    m = lst[0]
    for elem in lst:
        if elem < m:
            m = elem
    return m

def Tim_Khoang(lst):
    return Tim_Max(lst) if abs(Tim_Max(lst)) > abs(Tim_min(lst)) else Tim_min(lst)

lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
print("Giá trị x thỏa điều kiện là: ", Tim_Khoang(lst))