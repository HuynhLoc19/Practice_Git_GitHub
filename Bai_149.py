
    # Hãy nguyên hóa List bằng cách thay thế tất cả các phần tử trong List bằng số nguyên gần nó nhất

from random import *

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(round(uniform(-9, 10), 1))
    return lst

def Nguyen_Hoa(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = int(lst[i] + 0.5)
        else:
            lst[i] = int(lst[i] - 0.5)
    return lst

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List vừa đc tạo là: ', Tao_Lst(lst, n))
print('List sau khi nguyên hóa là: ', Nguyen_Hoa(lst))