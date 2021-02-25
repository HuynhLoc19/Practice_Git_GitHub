

# Tạo một mảng số nguyên có các giá trị khác nhau từng đôi một. Hãy liệt kê bộ ba giá trị x,y,z thỏa x=y+z

from random import *

def Tao_List(lst, n):
    for i in range(n):
        while True:
            elem = randrange(0, 30)
            flag = 0
            for i in range(len(lst)):
                if elem == lst[i]:
                    flag = 1
                    break
            if flag == 0:
                lst.append(elem)
                break
    return lst

def Liet_Ke(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            for k in range(len(lst)):
                if i!=j and j!=k and i!=k:
                    if lst[i] == lst[j] + lst[k]:
                        print(f'({lst[i]},{lst[j]},{lst[k]})', end=', ')


lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List vừa đc tạo là: ', Tao_List(lst, n))
Liet_Ke(lst)