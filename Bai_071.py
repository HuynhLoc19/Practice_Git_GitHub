

#   Đếm số lần xuất hiện của List A trong List B

from random import randrange

def Tao_Lst(lst, sl):
    for i in range(sl):
        #lst.append(randrange(0, 30))
        lst.append(int(input(f'Nhập phần tử lst[{i}]: ')))
    return lst

def K_Tra(lst_A, lst_B):
    dem = 0
    for i in range(len(lst_B)-len(lst_A)+1):
        flag = 1
        for j in range(len(lst_A)):
            if lst_A[j] != lst_B[i+j]:      #   <== Chú ý chỗ này: lst_B[i+j]
                flag = 0
                break
        if flag == 1:
            dem += 1
    return  dem

lst_A = []
n = int(input('Nhập số lượng phần tử của list A: '))
print('=> List A sau khi tạo là: ', Tao_Lst(lst_A, n))
lst_B = []
while True:
    m = int(input('\nNhập số lượng phần tử của list B: '))
    if m < n:
        print('List_B phải có nhiều phần tử hơn List_A!')
    else:
        break
print('=> List B sau khi tạo là: ', Tao_Lst(lst_B, m))
print('Số lần lst_A xuất hiện trong lst_B: ', K_Tra(lst_A, lst_B))