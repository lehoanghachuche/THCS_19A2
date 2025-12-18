s = input("Nhập chuỗi: ")
n = int(input("Nhập n: "))
tu = s.split()
print("Các từ có độ dài lớn hơn", n, "là:")
for t in tu:
    if len(t) > n:
        print(t)