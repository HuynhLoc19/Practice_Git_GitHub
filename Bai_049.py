
#    Tính trung bình cộng khoảng cách các cặp giá trọ trng List
from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))
    return lst

def TB_Cap(lst):
    S = 0
    dem = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                S += abs(lst[i] - lst[j])
                dem += 1
    return S/dem

lst = []
n = int(input('Nhập số lượng phần tử của list: '))
print('List đc tạo là: ', Tao_List(lst, n))
print('Trung bình cộng các khoảng cách trong List là: ', TB_Cap(lst))