n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(x)
max1 = a[0]
max2 = None
for x in a:
    if x > max1:
        max2 = max1
        max1 = x
    elif x != max1 and (max2 is None or x > max2):
        max2 = x
if max2 is None:
    print("Không có giá trị lớn thứ hai")
else:
    print("Giá trị lớn thứ hai là:", max2)