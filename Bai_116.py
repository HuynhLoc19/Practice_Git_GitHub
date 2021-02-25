
#   Viết hàm tìm tất cả các giá trị gần nhau nhất trong List

from random import *

def Tao_Lst(lst, n):
    for i in range(n):
        while True:
            elem = randrange(0, 5)
            flag = 0
            for j in range(len(lst)):
                if elem == lst[j]:
                    flag = 1
                    break
            if flag == 0:
                lst.append(elem)
                break
    return lst

def Distance_min(lst):
    lc = lst[0]
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if abs(lst[i]-lst[j]) < lc:
                lc = abs(lst[i]-lst[j])
    return lc

def Liet_Ke(lst):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if abs(lst[i]-lst[j]) == Distance_min(lst):
                print(f'({lst[i]},{lst[j]})', end=' ')

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List sau khi tạo là: ', Tao_Lst(lst, n))
print('Các cặp giá trị gần nhau nhất trong List là: ', end='')
Liet_Ke(lst)