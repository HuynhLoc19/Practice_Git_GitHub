# Hãy liệt kê các giá trị trong list các số nguyên tố có chư số đầu tiên là chữ số lẻ

from random import randrange

def Nhap_lst(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))

# Hàm kiểm tra số nguyên tố.
def kt_Nguyen_To(arr, elem):
    if elem == 2:
        return True
    elif elem < 2:
        return False
    else:
        if elem % 2 == 0:
            return False
        else:
            dem = 0
            for index in range(2, elem):
                if elem % index == 0:
                    dem += 1
            if dem != 0:
                return False
    return True

#Hàm ktra chữ số đầu tiên lẻ.
def Ktra(lst):
    for elem in lst:
        if (int(str(elem)[0]) % 2 != 0) and (kt_Nguyen_To(lst, elem) == True):
            print(elem,end=' ')


lst = []
n = int(input('Nhập số lượng phần tử của list: '))
Nhap_lst(lst, n)
print('List sau khi nhập là: ', lst)
print('Các số nguyên tố có chữ số đầu là số lẻ là: ')
Ktra(lst)