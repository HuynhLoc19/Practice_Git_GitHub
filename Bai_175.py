
    #   Hãy viết ct xuất List con từ List


from random import randrange

def Tao_Lst(lst, n):
    for i in range(n):
        lst.append(randrange(1, 20))
    return lst

def Lst_Con(lst):
    for i in range(1, len(lst)+1):
        print(f'List con có độ dài {i}: ')
        for j in range(len(lst)-i+1):
            C = []
            for k in range(j, i+j):
                C.append(lst[k])
            print(C)

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List sau khi đc tạo là: ', Tao_Lst(lst, n))
Lst_Con(lst)