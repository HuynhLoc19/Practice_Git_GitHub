
#   Liệt kê các ptu cực đại trong mảng một chiều các số thực


from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(-10, 30))
    return lst

def Lan_Can(lst):
    if lst[0]>lst[1]:
        print(lst[0], end=' ')
    for i in range(1, len(lst)-1):
        if lst[i]>lst[i-1] and lst[i]>lst[i+1]:
            print(lst[i], end=' ')
    if lst[len(lst)-1]>lst[len(lst)-2]:
        print(lst[len(lst)-1], end=' ')

lst = []
n = int(input('Các phần tử cực đại trong list: '))
Tao_List(lst, n)
print("List sau khi tạo là: ", lst)
print("Các giá trị thỏa điều kiện bài toán là: : ")
Lan_Can(lst)