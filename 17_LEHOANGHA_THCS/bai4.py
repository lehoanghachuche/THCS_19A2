with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write("ID,Ten san pham,Gia\n")
    f.write("1,Laptop,1200\n")
    f.write("2,Chuot may tinh,25\n")
    f.write("3,Ban phim,75\n")

id_can_sua = input("Nhập ID cần cập nhật: ")
gia_moi = input("Nhập giá mới: ")

ds_moi = []

with open("san_pham.txt", "r", encoding="utf-8") as f:
    for dong in f:
        parts = dong.strip().split(",")
        if parts[0] == id_can_sua:
            parts[2] = gia_moi
        ds_moi.append(",".join(parts))

with open("san_pham.txt", "w", encoding="utf-8") as f:
    for dong in ds_moi:
        f.write(dong + "\n")
