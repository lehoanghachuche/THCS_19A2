ds = [1, 2, 3, 4, 5, 6]
tong = 7
print("Các cặp số có tổng bằng", tong, "là:")
for i in range(len(ds)):
    for j in range(i + 1, len(ds)):
        if ds[i] + ds[j] == tong:
            print(ds[i], ds[j])