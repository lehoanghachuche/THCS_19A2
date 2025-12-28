ds_so = [1, 3, 5, 7, 9, 10, 12]

with open("so_nguyen.txt", "w", encoding="utf-8") as f:
    for so in ds_so:
        f.write(str(so) + "\n")