d = {
    "A": 30,
    "B": 60,
    "C": 80,
    "D": 45
}
ket_qua = {}
for key, value in d.items():
    if value > 50:
        ket_qua[key] = value
print("Các cặp thỏa mãn điều kiện:", ket_qua)