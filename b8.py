ds = [1, 2, 3, 4, 5]
k = int(input("Nhập k: "))
k = k % len(ds)  
ds_moi = ds[-k:] + ds[:-k]
print("List sau khi dịch chuyển:", ds_moi)