
#   Tìm giá trị dương nhỏ nhất trong List. Nếu List ko có giá trị dương nào thì trả về giá rị ko dương là 0

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 10))
    return lst

#   Hàm tìm giá trị dương đầu tiên trong List
def Duong_Dau(lst):
    for elem in lst:
        if elem > 0:
            return elem
    return 0

#   Hàm tìm giá trị dương nhỏ nhất
def Duong_min(lst):
    if Duong_Dau(lst) == 0:
        return 0
    lc = Duong_Dau(lst)
    for i in range(len(lst)):
        if lst[i] > 0 and lst[i] < Duong_Dau(lst):
            lc = lst[i]
    return lc


lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
print('Giá trị dương nhỏ nhất trong List là: ', Duong_min(lst))