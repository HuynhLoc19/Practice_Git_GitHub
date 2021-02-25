
    #   Hãy thêm một giá trị x vào trong List tăng mà vẫn giữu nguyên tính đơn điệu của List

def Tao_Lst(lst, n):
    for i in range(n):
        while True:
            elem = int(input(f'Nhập phần tử lst[{i}]: '))
            flag = 1
            for j in range(i):
                if elem < lst[j]:
                    flag = 0
                    break
            if flag == 0:
                print('Các phần tử trong List tăng dần. ')
            else:
                lst.append(elem)
                break
    return lst

def Them_Tang(lst, elem):
    i = 0
    while i < len(lst):
        if elem < lst[0]:
            lst.insert(0, elem)
            return lst
        if elem > lst[len(lst)-1]:
            lst.append(elem)
            return lst
        if elem > lst[i] and elem < lst[i+1]:
            lst.insert(i+1, elem)
            return lst
        i += 1

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List sau khi đc tạo là: ', Tao_Lst(lst, n))
x = int(input('Nhập giá tri x: '))
print(f'Lst sau khi thêm {x} vào: ', Them_Tang(lst, x))
