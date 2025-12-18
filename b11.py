n = int(input("Nhập kích thước ma trận n: "))
a = []
print("Nhập ma trận:")
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
doi_xung = True
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] != a[j][i]:
            doi_xung = False
            break
    if not doi_xung:
        break
if doi_xung:
    print("Ma trận là ma trận đối xứng")
else:
    print("Ma trận không phải là ma trận đối xứng")