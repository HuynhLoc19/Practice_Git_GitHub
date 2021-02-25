
# Hãy liệt kê các giá trị trong List thỏa đk lớn hơn trị tuyệt đối của giá trị đứng liền sau nó trong lIst

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

def Lien_Sau(lst):
    C = []
    for i in range(len(lst)):
        if i <= len(lst)-2:
            if lst[i] > abs(lst[i+1]):
                C.append(lst[i])
    return C

lst = []
n = int(input('Nhập số lượng phần tử trong list: '))
Tao_List(lst, n)
print("List sau khi tạo là: ", lst)
print("Các giá trị lớn hơn giá trị tuyệt đối của số liền sau nó là: ", Lien_Sau(lst))