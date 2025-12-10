la_so_nguyen_to = lambda n: n > 1 and all(n % i != 0 for i in range(2, n))
n = int(input("Nhập số nguyên dương n: "))
if la_so_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")
print("Các số nguyên tố trong khoảng từ 100 đến 500:")
for num in range(100, 501):
    if la_so_nguyen_to(num):
        print(num, end=" ")