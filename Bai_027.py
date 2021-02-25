
#    Hãy liệt kê các phtu trong List mà gái trị tại đó bằng giá trị âm đầu tiên trong List


from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(-10, 30))
    return lst

# HÀm tìm số âm đầu tiên trong mảng
def Am_Dau(lst):
    for elem in lst:
        if(elem < 0):
            return elem

# Hàm liệt kê
def Liet_Ke(lst):
    for elem in lst:
        if elem == Am_Dau(lst):
            print(elem, end=' ')

lst = []
n = int(input('Nhập số lượng phần tử trong list: '))
Tao_List(lst, n)
print("List sau khi tạo là: ", lst)
print("Các giá trị thỏa điều kiện bài toán là: : ")
Liet_Ke(lst)