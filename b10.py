m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
a = []
print("Nhập ma trận:")
for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)
max_tong = sum(a[0])
hang_max = 0

for i in range(1, m):
    tong = 0
    for j in range(n):
        tong += a[i][j]
    if tong > max_tong:
        max_tong = tong
        hang_max = i
print("Hàng có tổng lớn nhất là hàng:", hang_max)
print("Tổng lớn nhất là:", max_tong)