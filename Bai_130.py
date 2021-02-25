
#   Hãy cho biết các phần tử của List A có nằm  trong List B hay ko

from random import randrange

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(int(input(f'Nhập phần tử lst[{i}]: ')))
    return lst

def Ktra_List_Con(lst_A, lst_B):
    for i in range(len(lst_B) - len(lst_A) + 1):
        for j in range(len(lst_A)):
            if lst_A[j] != lst_B[i+j]:
                return 0

def Xuat_Kq(lst_A, lst_B):
    if Ktra_List_Con(lst_A, lst_B) == 0:
        print('Các phần tử trong Lst_A không nằm trong Lst_B.')
    else:
        print('Các phần tử trong Lst_A nằm trong Lst_B.')

lst_A = []
m = int(input('Nhập số lượng của Lst_A: '))
print('List A sau khi đc tạo là: ', Tao_Lst(lst_A, m))

lst_B = []
while True:
    n = int(input('Nhập số lượng của Lst_B: '))
    if n < m:
        print('Số lượng phần tử của Lst_B phải lớn hơn Lst_A. ')
    else:
        break
print('List B sau khi đc tạo là: ', Tao_Lst(lst_B, n))
Xuat_Kq(lst_A, lst_B)