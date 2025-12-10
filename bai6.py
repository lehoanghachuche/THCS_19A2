def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def in_so_nguyen_to_trong_khoang(a, b):
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            print(i, end=" ")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
in_so_nguyen_to_trong_khoang(a, b)