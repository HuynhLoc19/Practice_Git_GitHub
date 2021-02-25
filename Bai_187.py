
    #   Tìm dãy con TOÀN DƯƠNG có TỔNG LỚN NHẤT trong List

from random import randrange

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(int(input(f'Nhập giá trị của lst[{i}]: ')))
    return lst

def Tinh_Tong(lst, i, j):
    S = 0
    for k in range(j, i+j):
        S += lst[k]
    return S

def Ktra_Toan_Duong(lst, i, j):
    for k in range(j, i+j):
        if lst[k] < 0:
            return False
    return True

def Duong_Dau(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            return i
    return 0

def Duong_Max(lst):
    index_i_M = 2
    index_j_M = Duong_Dau(lst)
    for i in range(2,len(lst)+1):
        for j in range(len(lst)-i+1):
            if Ktra_Toan_Duong(lst, i, j) and Tinh_Tong(lst, i, j) > Tinh_Tong(lst, index_i_M, index_j_M):
                index_i_M = i
                index_j_M = j
    C = []
    for i in range(index_j_M, index_i_M + index_j_M):
        C.append(lst[i])
    return C

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List sau khi đc tạo là: ', Tao_Lst(lst, n))
print('List con toàn dương có tổng lớn nhất: ', Duong_Max(lst))