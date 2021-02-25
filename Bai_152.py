
#   Đưa các số nguyên tố về cuối List

from random import randrange

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(1, 20))
    return lst

def Kt_Ng_To(n):
    if n == 2:
        return True
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def Xep_NgTo_Cuoi(lst):
    vt = len(lst)-1
    for i in range(len(lst)-1, -1, -1):
        if Kt_Ng_To(lst[i]):
            tam = lst[i]
            lst[i] = lst[vt]
            lst[vt] = tam
            vt -= 1
    return lst

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List sau khi đc tạo là: ', Tao_Lst(lst, n))
print('List sau khi xếp các số nguyên tố vào cuối là: ', Xep_NgTo_Cuoi(lst))