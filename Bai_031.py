

# Tạo một mảng số nguyên có các giá trị khác nhau từng đôi một. Hãy liệt kê các cặp giá trị nằm trong List [x<=y]

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

def Tao_Hai(lst):
    for i in range(len(lst)):
        print('\n => Phần tử thứ', i+1, ': ', end='')
        for j in range(len(lst)):
            if lst[i] <= lst[j] and i != j:
                print('('+str(lst[i])+','+str(lst[j])+'),', end=' ')

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List vừa đc tạo là: ', Tao_List(lst, n))
Tao_Hai(lst)