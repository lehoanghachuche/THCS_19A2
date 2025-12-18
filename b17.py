d = {1: 10, 2: 25, 3: 15, 4: 25}
max_value = None
max_key = None
for key in d:
    if max_value is None or d[key] > max_value:
        max_value = d[key]
        max_key = key
print("Key có giá trị lớn nhất là:", max_key)
print("Giá trị lớn nhất là:", max_value)