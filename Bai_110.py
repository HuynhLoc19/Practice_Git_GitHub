
#   Tìm số nguyên tố nhỏ nhất lớn hơn tất cả các giá trị có trong List

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

#   Hàm kiểm tra số nguyên tố
def kt_NgTo(elem):
    if elem < 2:
        return False
    elif elem == 2:
        return True
    else:
        if elem % 2 == 0:
            return False
        for i in range(2, elem):
            if elem % i == 0:
                return False
    return True

#   Hàm tìm gái trị lớn nhất trong List
def MAX(lst):
    M = lst[0]
    for elem in lst:
        if elem > M:
            M = elem
    return M

#   Hàm tìm số nguyên tố nhỏ nhất lớn hơn tất cả các giá trị trong Lst
def Ng_To_min(lst):
    lc = MAX(lst) + 1
    while kt_NgTo(lc) == False:
        lc += 1
    return lc


lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
print('Số nguyên tố nhỏ nhất lớn hơn tất cả các phần tử trong List là: ', Ng_To_min(lst))
