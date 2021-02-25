
#    Đếm sl các số nguyên tố phân bệt trong List

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

#   Hàm ktra số nguyên tố.
def kt_NgTo(elem):
    if elem == 2:
        return True
    elif elem < 2:
        return False
    else:
        if elem % 2 == 0:
            return False
        else:
            for i in range(2, elem-1):
                if elem % i == 0:
                    return False
    return True

#    Hàm đếm số lượng số nguyên tố phân biệt:
def Dem_SL(lst):
    dem = 0
    for i in range(len(lst)):
        flag = 0
        for j in range(i):
            if lst[j] == lst[i]:
                lag = 1
                break
        if flag == 0 and kt_NgTo(lst[i]):
            print("=> Số nguyên tố phân biệt của List là: ", lst[i])
            dem += 1
    return dem

lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
print('Số lượng các số nguyên tố phân biệt trong List là: ', Dem_SL(lst))