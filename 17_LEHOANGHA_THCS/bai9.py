def tinh_tong_chu_so(n):
    if n < 10:          
        return n
    else:
     (n % 10) + tinh_tong_chu_so(n // 10)
n = int(input("Nhập số nguyên dương n: "))
print("Tổng các chữ số là:", tinh_tong_chu_so(n))