import sys
import os
duong_dan = os.path.abspath("../thu_vien_chung")
sys.path.append(duong_dan)
import xu_ly_so
so = 7
if xu_ly_so.kiem_tra_so_nguyen_to(so):
    print(so, "là số nguyên tố")
else:
    print(so, "không phải số nguyên tố")