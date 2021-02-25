


# Hãy liệt kê các giá trị chẵn trong mảng một chiều các số nguyên thuộc đoạn [x,y] cho trước.

from random import randrange

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(0,30))
    return lst

def kt_List(lst, x, y):
    for i in range(len(lst)):
        if (lst[i] >= x) and (lst[i] <= y):
            if (lst[i] % 2 == 0):
                print(lst[i], end=' ')

lst = []
n = int(input('Nhập số lượng phần tử trong lst: '))
x = int(input('Nhập x: '))
y = int(input('Nhập y: '))
Tao_Lst(lst, n)
print('List được tạo là: ', lst)
print('Các giá trị chẵn trong lst thuộc đoạn [{0},{1}] là: '.format(x, y))
kt_List(lst, x, y)