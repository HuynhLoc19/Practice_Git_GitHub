
#  Hãy liệt kê các giá trị trong List thỏa nhỏ hơn trị tuyệt đối của số liền sau nó và đồng thời

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

def Sau_Truoc(lst):
    C = []
    for i in range(len(lst)):
        if i <= len(lst)-2 and i>=1:
            if lst[i] > abs(lst[i-1]) and lst[i] < abs(lst[i+1]):
                C.append(lst[i])
    return C

lst = []
n = int(input('Nhập số lượng phần tử trong list: '))
Tao_List(lst, n)
print("List sau khi tạo là: ", lst)
print("Các giá trị thỏa điều kiện bài toán là: : ", Sau_Truoc(lst))