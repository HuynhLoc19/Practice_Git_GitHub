
#   Kiểm tra xem LIST có tồn tại giá trị 0 ko. Nếu có trẩ về giá trị +1, ko thì trả về giá trị 0

from random import randrange

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(0,5))
    return lst

def K_Tra(lst):
    for elem in lst:
        if elem==0:
            return 1
    return 0

lst = []
n = int(input('Nhập số lượng hần tử của List: '))
print('List vừa tạo là: ', Tao_Lst(lst, n))
print(K_Tra(lst))