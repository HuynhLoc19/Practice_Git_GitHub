# Định nghĩa hàm xây dựng mảng b từ mảng a các số nguyên sao cho mảng b chỉ chứa các giá trị đối xứng trong list.

from random import randrange
#from time import sleep

def Nhap_lst(lst, n):
    for i in range(n):
        lst.append(randrange(0, 1000))

def kt_Doi_Xung(lst):
    DX = []
    for i in lst:
        elem = str(i)
        if elem == elem[::-1]:
            DX.append(i)
    return DX

#   Thêm số 0 vào sau các giá trị lẻ có trong list
def Them_0(lst):
    for i in range(len(lst)-1, -1, -1):
        print(len(lst))
        if lst[i] % 2 != 0:
            lst.insert(i+1, 0)
    return lst

'''def Them_0(lst):
    i = 0
    while i<len(lst):
        if lst[i] % 2 != 0:
            lst.insert(i + 1, 0)
        i += 1
    return lst'''



lst = []
n = int(input('Nhập số lượng phần tử của list: '))
Nhap_lst(lst, n)
print('List sau khi nhập là: ', lst)
print('Các phần tử đối xứng trong List là: ', kt_Doi_Xung(lst))
print('List sau khi đc thêm 0 vào sau những phần tử lẻ: ', Them_0(lst))