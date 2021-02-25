
#  Tìm ktra và trả về số nguyên tố cuối cùng trong List

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 10))
    return lst

#   Hàm ktra số nguyên tố
def kt_NgTo(elem):
    if elem < 2:
        return False
    elif elem == 2:
        return True
    else:
        if elem % 2 == 0:
            return False
        for i in range(2, elem):
            if elem % i == 0:
                return False
    return True

#   Hàm trả về số nguyên tố cuối cùng
def NgTo_Cuoi(lst):
    for i in range(len(lst)-1, -1, -1):
        if kt_NgTo(lst[i]):
            return lst[i]
    return 0

lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
print('Số nguyên tố cuối cùng của List là: ', NgTo_Cuoi(lst))