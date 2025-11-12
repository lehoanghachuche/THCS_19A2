luong_co_ban = float(input("Nhập số lương cơ bản: "))
ngay_cong = float(input("Nhập số ngày công: "))
luong_mot_ngay = luong_co_ban / 22 
luong_thuc_te = luong_mot_ngay * ngay_cong
if ngay_cong > 22:
    thuong = luong_thuc_te * 0.10
    phat = 0
if ngay_cong < 22:
    thuong = 0
    phat = luong_thuc_te * 0.05
tong_luong = luong_thuc_te + thuong - phat    
print(f"Lương thực tế của nhân viên là:  {luong_thuc_te:,.0f} VNĐ ")        
print(f"Tiền phạt là:  {phat:,.0f} VNĐ")
print(f"Tiền thưởng là:  {thuong:,.0f} VNĐ")
print(f"Số tiền trả cho nhân viên: {tong_luong:,.0f} VNĐ ")
