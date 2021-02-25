
#    Hãy liệt kê các vị trí mà giá trọ tại đó bằng giá trị dương min trong List

from random import randrange

def Tao_List(lst, n):
    for i in range(n):
        lst.append(randrange(-10, 30))
    return lst

# Hàm tìm số dương đầu tiên trong List
def Duong_Dau(lst):
      for elem in lst:
          if elem > 0:
              return elem

# Hàm tìm số dương nhỏ nhất trong list
def Duong_min(lst):
    m = Duong_Dau(lst)
    for elem in lst:
        if(elem > 0 and elem < m):
            m = elem
    return m

# Hàm liệt kê
def Liet_Ke(lst):
    for i in range(len(lst)):
        if lst[i] == Duong_min(lst):
            print(i, end=' ')

lst = []
n = int(input('Nhập số lượng phần tử trong list: '))
Tao_List(lst, n)
print("List sau khi tạo là: ", lst)
print('Các vị trí mà giá trị tại đó bằng giá trị dương nhỏ nhất', Duong_min(lst), ' là: : ')
Liet_Ke(lst)