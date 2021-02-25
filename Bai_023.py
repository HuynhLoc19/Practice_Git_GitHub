
#   Liệt kê các giá trị chẵn có ít nhất một lân cận cũng là giá trị chẵn

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

def Lan_Can(lst):
    if lst[0]%2==0 and lst[1]%2==0:
        print(lst[0], end=' ')
    for i in range(1, len(lst) - 1):
        if lst[i]%2==0 and lst[i+1]%2==0 or lst[i]%2==0 and lst[i-1]%2==0:
            print(lst[i], end=' ')
    if lst[len(lst)-1]%2==0 and lst[len(lst)-2]%2==0:
        print(lst[len(lst) - 1], end=' ')

lst = []
n = int(input('Nhập số lượng phần tử trong list: '))
Tao_List(lst, n)
print("List sau khi tạo là: ", lst)
print("Các giá trị thỏa điều kiện bài toán là: : ")
Lan_Can(lst)