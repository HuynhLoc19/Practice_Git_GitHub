
#   Liệt kê và đếm số lượng giá trị chỉ xuất hiện một trong hai List A hoặc B

from random import randrange

def Tao_Lst(lst, sl):
    for i in range(sl):
        lst.append(randrange(0, 30))
    return lst

# Hàm kiểm tra phàn tử trong Lst_A có xuất hiện trong Lst_B không?
def Tan_Suat(lst, ptu):
    for elem in lst:
        if elem == ptu:
            return False
    return True

def Dem_Ph_Biet(lst, lst_n):
    dem = 0
    for i in range(len(lst)):
        flag = 0
        for j in range(i):
            if lst[j] == lst[i]:
                flag = 1
                break
        if flag == 0:
            if Tan_Suat(lst_n, lst[i]):
                print(lst[i], end=' ')
                dem += 1
    return dem

lst_A = []
n = int(input('Nhập số lượng phần tử của list A: '))
print('=> List A sau khi tạo là: ', Tao_Lst(lst_A, n))
lst_B = []
m = int(input('\nNhập số lượng phần tử của list B: '))
print('=> List B sau khi tạo là: ', Tao_Lst(lst_B, m))
print('\n=> Các giá trị chỉ xuất hiện một trong hai List A hoặc B là: ', end='')
print('\n=> Số lượng các giá trị chỉ xuất hiện một trong hai List là: ', Dem_Ph_Biet(lst_A, lst_B) + Dem_Ph_Biet(lst_B, lst_A))


