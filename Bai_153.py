    #   Hãy đứa các số chẵn về đâu danh sách, các số lẻ về cuối danh sách và các soos 0 về giưã

from random import randrange

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(1, 20))
    return lst

def Sap_Xep(lst):
    vt = 0
    for i in range(n):
        if lst[i] % 2 == 0:
            tam = lst[i]
            lst[i] = lst[vt]
            lst[vt] = tam
            vt += 1
    vt_n = len(lst)-1
    for i in range(len(lst)-1, -1, -1):
        if lst[i] % 2 != 0:
            tam = lst[i]
            lst[i] = lst[vt_n]
            lst[vt_n] = tam
            vt -= 1
    return lst

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List sau khi đc tạo là: ', Tao_Lst(lst, n))
print('List sau khi sắp xếp là: ', Sap_Xep(lst))