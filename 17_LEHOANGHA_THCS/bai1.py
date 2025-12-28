with open("vanban.txt", "w", encoding="utf-8") as f:
    f.write(noi_dung)
with open("vanban.txt", "r", encoding="utf-8") as f:
    text = f.read()
so_tu = len(text.split())
print("Tổng số từ:", so_tu)