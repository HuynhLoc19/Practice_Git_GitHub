
#   Tính tổng các gái trị đối xứng trong List

from random import *

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(100, 500))
    return lst

# Hàm đệ quy tìm số đảo ngược
def Dao_Nguoc(elem, dn):
    if elem==0:
        return dn
    dn = dn*10 + elem%10
    return Dao_Nguoc(elem//10, dn)

# Hàm tính ttoongr các giá trị đối xứng trong List
def Tong_DX(lst):
    S = 0
    for i in range(len(lst)):
        if lst[i] == Dao_Nguoc(lst[i], 0):
            S += lst[i]
    return S

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List vừa đc tạo là: ', Tao_List(lst, n))
print('Tổng các chữ số đảo ngược trong List là: ', Tong_DX(lst))