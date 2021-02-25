
#   Đảo ngược các giá trị chẵn có trong List, các giá tị lẻ giữu nguyên vị trí

from random import randrange

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(1, 20))
    return lst

def Dao_Chan(lst):
    C = []
    for i in range(len(lst)-1, -1, -1):
        if lst[i] % 2 == 0:
            C.append(lst[i])
    vt = 0
    for i in range(n):
        if lst[i] % 2 == 0:
            lst[i] = C[vt]
            vt += 1
    return lst

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List sau khi đc tạo là: ', Tao_Lst(lst, n))
print('List sau khi dảo ngược các giá trị chẵn là: ', Dao_Chan(lst))