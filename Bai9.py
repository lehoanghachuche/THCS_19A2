so_kwh = float(input("Nhập số kwh điện đã tiêu thụ:"))
if so_kwh <= 100:
    tien = so_kwh * 1678
if so_kwh <= 200:
    tien = so_kwh  * 1734
if so_kwh <= 300:
    tien = so_kwh * 2014
print(f"Tổng số tiền phải trả là: {tien:,} VNĐ")