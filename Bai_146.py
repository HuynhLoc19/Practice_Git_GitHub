
#   Hãy trộn hai List tăng dần thành một List tăng dần


def Tao_Lst(lst, n):
    for i in range(n):
        while True:
            elem = int(input(f'Nhập phần tử lst[{i}]: '))
            flag = 1
            for j in range(len(lst)):
                if elem < lst[j]:
                    flag = 0
                    break
            if flag == 0:
                print('Các phần tử trong list phải tăng dần. ')
            else:
                lst.append(elem)
                break
    return lst

def Tron_Lst(lst_A, lst_B):
    C = []
    for i in range(len(lst_A)):
        C.append(lst_A[i])
    for j in range(len(lst_B)):
        C.append(lst_B[j])
    for m in range(len(C)):
        for n in range(m+1, len(C)):
            if C[n] < C[m]:
                C[n] = C[n] + C[m]
                C[m] = C[n] - C[m]
                C[n] = C[n] - C[m]
    return C

lst_A = []
m = int(input('Nhập số lượng của Lst_A: '))
print("Lst A sau khi tạo là: ", Tao_Lst(lst_A, m))

lst_B = []
n = int(input('Nhập số lượng của Lst_B: '))
print("Lst B sau khi tạo là: ", Tao_Lst(lst_B, n))

print('List tăng dần sau khi trộn hai list A và B là: ', Tron_Lst(lst_A, lst_B))

