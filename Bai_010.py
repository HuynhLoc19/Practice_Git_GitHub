


# Hãy liệt kê các phần tử toàn chẵn trong List

from random import randrange

def Nhap_lst(lst, n):
    for i in range(n):
        lst.append(randrange(0, 30))

# Hàm đệ quy ktra một chữ số có toàn chẵn hay ko
def kt_Toan_Chan(elem):
    if elem == 0:
        return True
    if (elem % 10)%2 != 0:
        return False
    return kt_Toan_Chan(elem//10)

def Goi_Ham(lst):
    C = []
    flag = 1
    for elem in lst:
        if kt_Toan_Chan(elem) == False:
            flag = 0
            C.append(elem)
    if flag == 1:
        print('Các chữ số của mỗi phần tử trong List toàn chẵn.')
    else:
        print('List có phần tử có chữ số lẻ.')
    return C

lst = []
n = int(input('Nhập số lượng phần tử của list: '))
Nhap_lst(lst, n)
print('List sau khi nhập là: ', lst)
print('Câc giá trị lẻ trong List: ', Goi_Ham(lst))
