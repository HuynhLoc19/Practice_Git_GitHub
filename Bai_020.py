
# Hãy liệt kê các phần tử cực tiểu trong list. Một phần tử đc gọi là cực tiểu khi nhỏ hơn các phần tử lân cận

from random import randrange

def Tao_Mang(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

def kt_Cuc_Tieu(lst):
    if lst[0] < lst[1]:
        print(lst[0], end=' ')
    for i in range(1, len(lst) - 1):
        if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
            print(lst[i], end=' ')
    if lst[len(lst)-1] < lst[len(lst)-2]:
        print(lst[len(lst)-1], end=' ')

lst = []
n = int(input('Nhập số lượng phần tử của list: '))
Tao_Mang(lst, n)
print('Mảng sau khi tạo là: ', lst)
print('Các phần tử cực đại của List là: ')
kt_Cuc_Tieu(lst)
