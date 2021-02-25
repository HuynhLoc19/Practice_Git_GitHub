
    # Dịch trái xoay vòng các phần tử trong List


from random import randrange

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(1, 20))
    return lst

def Trai_Xoay_Vong(lst):
    tam = lst[0]
    for i in range(len(lst)-1):
        lst[i] = lst[i+1]
    lst[len(lst)-1] = tam
    return lst

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List sau khi đc tạo là: ', Tao_Lst(lst, n))
print('List sau khi được dịch trái xoay vòng là: ', Trai_Xoay_Vong(lst))