
#  Tìm ktra và trả về số đối xứng đầu tiên trong List

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(100, 300))
    return lst

#   Hàm ktra số đối xứng bằng ĐỆ QUY
def Doi_Xung(elem, dn):
    if elem == 0:
        return dn
    dn = dn*10 + elem%10
    return Doi_Xung(elem//10, dn)

#   Hàm ktra và trả về số đối xứng đầu tiên trọng List
def Tra_Ve(lst):
    for elem in lst:
        if Doi_Xung(elem, 0) == elem:
            return elem
    return 10

lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
print('Số đối xứng đầu tiên trong List là: ', Tra_Ve(lst))