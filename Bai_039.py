
# Tìm các số trong List có chữ só đầu tiên là chữ số lẻ

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

# Hàm tìm số có chữu số đầu tiên là chữu số chẵn
def Dau_Tien(lst):
    for elem in lst:
        t = elem
        while t >= 10:
            t //= 10
        if t % 2 == 0:
            print(elem, end=' ')


lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
print('Các số có chữ số đầu tiên là chữ số chẵn là: ', end='')
Dau_Tien(lst)