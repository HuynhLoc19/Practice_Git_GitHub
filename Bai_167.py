
    #   Hãy xóa tất cả các phần tử trùng nhau và chỉ giữ lại một phần tử duy nhất


from random import randrange

def Tao_Lst(lst, n): 
    for i in range(n):
        lst.append(randrange(1, 10))
    return lst

def Xoa_Trung(lst):
    # Xóa phần tử thì phải duyệt từ cuối dsách về đầu, nếu duyệt ngược lại thì sẽ sót phần tử
    for i in range(len(lst)-1, -1, -1):
        # Duyệt danh sách ktra từ đầu dsach đến trước phần tử trong for..loop hiện tại có xuất hiện phàn tử nào giống nó ko
        for j in range(len(lst)-1, i, -1):
            #   Nếu có thì xóa phần tử j đó
            if lst[i] == lst[j]:
                del lst[j]
    return lst

lst = []
n = int(input('Nhập số lượng phần tử của List: '))
print('List sau khi đc tạo là: ', Tao_Lst(lst, n))
print('List sau khi xoa cac phan tu trung: ', Xoa_Trung(lst))