gia = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))
tong_chi_phi = gia * so_luong
thue_vat =tong_chi_phi * 0.10 
tong_tien =tong_chi_phi + thue_vat
print("Tổng chi phí: ", round(tong_chi_phi,))
print("Thuế VAT (10%):", round(tong_chi_phi))
print("Tổng tiền phải trả: ", round(tong_tien))

                        
