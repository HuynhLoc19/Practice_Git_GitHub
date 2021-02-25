
#   Tìm chữ số xuất hiện nhiều nhất trong List

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

#   Hàm đếm từng chữ số trong List
def Chu_So(lst, index):
    dem = 0
    for elem in lst:
        if elem == 0:
            dem += 1
        t = elem
        while t != 0:
            if t%10 == index:
                dem += 1
            t //= 10
    return dem

def Dem_Chu_So(lst, C):
    for i in range(0, 10 ):
        C.append(Chu_So(lst, i))
    for i in range(len(C)):
        print(f'=> Phần tử {i} có {C[i]} lần trong List.')
    return C

#   Hàm tìm chữ số xuất hiện nhiều nhất trong List
def Xuat_Hien(C):
    lc = 0
    for i in range(len(C)):
        if C[i] > C[lc]:
            lc = i
    return lc

lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
C = []
C = Dem_Chu_So(lst, C)
print('Chữ số xuất hiện nhiều nhất trong List là: ', Xuat_Hien(C))