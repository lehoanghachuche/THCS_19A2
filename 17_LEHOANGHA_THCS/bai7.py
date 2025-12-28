import os
os.makedirs("thu_muc_a/thu_muc_b", exist_ok=True)
open("thu_muc_a/file1.txt", "w").close()
open("thu_muc_a/thu_muc_b/file2.txt", "w").close()
print(os.listdir("thu_muc_a"))