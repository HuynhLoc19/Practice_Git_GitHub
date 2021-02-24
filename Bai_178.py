
    #   Xuất và tính tổng từng Lst con tăng trong Lst các số nguyên

from random import randrange

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(1, 20))
    return lst

#   Hàm tính tổng Lst con tăng
def Tong_Tang(C):
    S = 0
    for elem in C:
        S += elem
    return S

def Lst_Tang(lst):
    #   Vòng lặp FOR để xét các Lst con có i phần tử
    for i in range(2, len(lst)+1):
        print(f'\n****** Lst tăng gồm {i} phần tử ******')
        for j in range(len(lst)-i+1):
            # Tạo một Lst C con để thêm các phần tử cả Lst con tăng vào
            C = []
            #   Ktra xem List con hiện tại có phải là một lst tăng hay ko
            flag = 1
            for k in range(j, i+j-1):   # -1 để không bị lỗi "k out of range", nếu ko -1, khi k = len(lst)-1 thì k+1=len(lst) bị lỗi "out of range"
                #   Nếu trong Lst đag ktra xuất hiện 1 cặp giá trị ko tăng thì gán flag=0 và thoát khỉ vòng lặp htai-> Ktra vòng lặp khác
                if lst[k] >= lst[k+1]:
                    flag = 0
                    break
            #   Nếu Lst đag ktra là tăng thì tạo 1 Lst con mới và xuất ra màn hình
            if flag == 1:
                #   Vòng lặp FOR thêm gái trị của Lst tăng vào 1 LIST C mới và xuất ra màn hình
                for k in range(j, i + j):
                    #   Phương thức append để thêm từng phần tử của Lst tăng vào C
                    C.append(lst[k])
                #   Xuất từng Lst C ra màn hình
                print('=>', C)
                print('=> Tổng các phần tử của Lst: ', Tong_Tang(C))

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List sau khi đc tạo là: ', Tao_Lst(lst, n))
print('======== CÁC LST CON TĂNG DẦN ========')
Lst_Tang(lst)

print('Loc dep trai vai dai')
print('Cuoc song nay chi co lam thi moi co an')
print('Khong lam ma doi co an thi chi an dau bua, an cam.')
