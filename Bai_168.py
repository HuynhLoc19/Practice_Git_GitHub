

    #   Xóa tất cả các phần tử có tần suất xuất hiện nhiều hơn một lần trong List

from random import randrange

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(1, 10))
    return lst

#   Hàm đếm tần suất xhien của phần tử elem trong List
def Dem_TSuat(lst, ptu):
    dem = 0
    for elem in lst:
        if elem == ptu:
            dem += 1
    return dem

#   Hàm xóa tất cả các phần tử trùng trong List
def  Xoa_Trung(lst, elem):
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == elem:
            del lst[i]
    return lst

#   Hàm tìm các ptu ph.biệt của Lst và xóa các phần tử trong Lst có tần suất xhien nhiều hơn 1 trong Lst
def PTu_PBiet(lst):
    for i in range(len(lst)-1, -1, -1):
        flag = 0
        for j in range(i):
            if lst[i] == lst[j]:
                flag = 1
                break
        if flag == 0:
            if Dem_TSuat(lst, lst[i]) > 1:
                Xoa_Trung(lst, lst[i])
    return lst

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List sau khi đc tạo là: ', Tao_Lst(lst, n))
print('Lst sau khi xóa các phần tử có tần suất xhien nhiều hơn 1 lần trong Lst: ', PTu_PBiet(lst))