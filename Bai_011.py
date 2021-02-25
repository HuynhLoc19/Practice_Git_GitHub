
from random import randrange

def Nhap_lst(lst, n):
    for i in range(n):
        lst.append(randrange(0, 10))

def kt_3m(lst):
    C = []
    for elem in lst:
        flag = 1
        t = elem
        while t > 1:
            if t % 3 == 0:
                t /= 3
                continue
            else:
                flag = 0
                break
        if flag == 1 and elem > 1:
            C.append(elem)
    return C

lst = []
n = int(input('Nhập số lượng phần tử của list: '))
Nhap_lst(lst, n)
print('List sau khi nhập là: ', lst)
print('Các phần tử có dạng 3^m là: ', kt_3m(lst))
