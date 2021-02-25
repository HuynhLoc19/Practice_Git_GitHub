
#   HÃy liệt kê số lần xuất hiện của các giá trị có trong List

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

def Dem_SL(lst):
    for i in range(len(lst)):
        flag = 0
        for j in range(i):
            if lst[j] == lst[i]:
                flag = 1
                break
        dem = 0
        if flag == 0:
            for elem in lst:
                if lst[i] == elem:
                    dem += 1
            print(f'=> Phần tử {lst[i]} xuất hiện {dem} lần trong List.')

lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
Dem_SL(lst)