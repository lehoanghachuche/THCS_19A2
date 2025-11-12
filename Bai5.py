tien_gui = float(input("Nhập số tiền gửi ban đầu(VNĐ):" ))
lai_suat_nam = float (input("Nhập lãi suất hàng năm(%):" ))
lai_suat = lai_suat_nam / 100
lai_1_thang = tien_gui * lai_suat * (1/12)
lai_2_quy = tien_gui * lai_suat * (6/12)
lai_3_nam = tien_gui * lai_suat * 3
print("Tiền gửi 1 tháng: ", round(lai_1_thang), ("VNĐ"))
print("Tiền lãi 2 quý: " , round(lai_2_quy) , ("VNĐ"))
print("Tiền lãi 3 năm:" ,round(lai_3_nam) , ("VNĐ"))
                