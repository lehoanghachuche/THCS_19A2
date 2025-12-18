n = int(input("Nhập kích thước ma trận n: "))
a = []
print("Nhập các phần tử của ma trận:")
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
tong = 0
for i in range(n):
    tong += a[i][n - 1 - i]
print("Tổng các phần tử trên đường chéo phụ là:", tong)