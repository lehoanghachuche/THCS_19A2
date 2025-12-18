m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
a = []
print("Nhập ma trận:")
for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)
if m != n:
    print("Ma trận không phải là ma trận vuông")
else:
    la_don_vi = True
    for i in range(n):
        for j in range(n):
            if i == j:
                if a[i][j] != 1:
                    la_don_vi = False
                    break
            else:
                if a[i][j] != 0:
                    la_don_vi = False
                    break
        if not la_don_vi:
            break
    if la_don_vi:
        print("Ma trận là ma trận đơn vị")
    else:
        print("Ma trận không phải là ma trận đơn vị")