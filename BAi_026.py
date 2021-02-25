
#    hãy liệt kê các phần tử cực trị trong List. Một phần tử đc goi là cực trị khi nó là cực đại or cực tiểu


from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(-10, 30))
    return lst

def Lan_Can(lst):
    if lst[0] != lst[1]:
        print(lst[0], end=' ')
    for i in range(1, len(lst)-1):
        if (lst[i]>lst[i-1] and lst[i]>lst[i+1]) or (lst[i]<lst[i-1] and lst[i]<lst[i+1]):
            print(lst[i], end=' ')
    if lst[len(lst)-1] != lst[len(lst)-2]:
        print(lst[len(lst)-1], end=' ')

lst = []
n = int(input('Nhập sô lượng các phần tử trong list: '))
Tao_List(lst, n)
print("List sau khi tạo là: ", lst)
print("Các phần tử cực trị trong List: ")
Lan_Can(lst)