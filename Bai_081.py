
from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(1950, 3000))
    return lst

def Dau(lst):
    for elem in lst:
        if elem>2005:
            return elem
    return 0

lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
print(Dau(lst))
