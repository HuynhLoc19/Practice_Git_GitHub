# Xuất tất cả list con có độ dài l trong list

from random import randrange

def Nhap_lst(lst, n):
    for i in range(n):
        lst.append(randrange(0, 1000))
def Mang_Con(lst, l):
    for i in range(len(lst)):
        C = []
        for j in range(i, i+l):
            C.append(lst[j])
        print('Mảng',i+1,': ', C)
        if len(lst) - 1 - i < l:
            break

lst = []
n = int(input('Nhập số lượng phần tử của list: '))
Nhap_lst(lst, n)
print('List sau khi nhập là: ', lst)
l = int(input('Nhập chiều dài mảng con: '))
Mang_Con(lst, l)
