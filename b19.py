ds = {
    "An": 8,
    "Bình": 9,
    "Chi": 8,
    "Dũng": 7,
    "Hà": 9
}
ket_qua = {}
for ten, diem in ds.items():
    if diem not in ket_qua:
        ket_qua[diem] = [ten]
    else:
        ket_qua[diem].append(ten)
print(ket_qua)