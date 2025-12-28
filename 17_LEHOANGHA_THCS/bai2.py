with open("vanban.txt", "r", encoding="utf-8") as f:
    text = f.read()
tu_list = text.split()
tan_suat = {}
for tu in tu_list:
    tu = tu.lower().strip(".,")
    tan_suat[tu] = tan_suat.get(tu, 0) + 1
for tu, so_lan in tan_suat.items():
    print(f"{tu}: {so_lan}")
