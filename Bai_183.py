
    #   Tìm List dương dài nhất trong List

from random import randrange

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(-10, 20))
    return lst

def Ktra_Toan_Duong(lst, j, i):
    for k in range(j, i+j):
        if lst[k] < 0:
            return False
    return True

def Ktra_Dai(lst):
     for i in range(len(lst), 1, -1):
         for j in range(len(lst)-i+1):
             C = []
             if Ktra_Toan_Duong(lst, j, i):
                 for k in range(j, i + j):
                    C.append(lst[k])
                 return C

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List sau khi đc tạo: ', Tao_Lst(lst, n))
print('List con toàn dương dài nhất trong List: ', Ktra_Dai(lst))