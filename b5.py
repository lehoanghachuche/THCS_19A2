a = list(map(int, input("Nhập các phần tử: ").split()))
ket_qua = []
for x in a:
    if x not in ket_qua:
        ket_qua.append(x)
print("Danh sách sau khi loại bỏ trùng lặp:")
print(ket_qua)