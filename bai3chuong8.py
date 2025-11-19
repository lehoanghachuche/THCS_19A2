import math
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
g = math.gcd(tu,mau)
tu //= g 
mau //= g
print("Phân số tối giản: " , tu , mau )