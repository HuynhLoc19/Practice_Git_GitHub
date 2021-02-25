
#   Viết hàm liệt kê các số xuất hiện nhiều hơn một lần trong Lst
from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

#   Hàm đếm số lần xuất hiện của phần tử trong List
def Dem_Sl(lst, ptu):
    dem = 0
    for elem in lst:
        if elem == ptu:
            dem += 1
    return dem

#   Hàm liệt kê số lượng các phần tử xuất hiện nhiều hơn một lần trong List
def So_Ph_Biet(lst):
    for i in range(len(lst)):
        flag = 0
        for j in range(i):
            if lst[j] == lst[i]:
                flag = 1
                break
        if flag == 0:
            if Dem_Sl(lst, lst[i]) > 1:
                print(f'Phần tử {lst[i]} xuất hiện {Dem_Sl(lst, lst[i])} lần trong List.')


lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
So_Ph_Biet(lst)