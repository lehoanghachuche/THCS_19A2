def chuyen_doi_nhiet_do(do_C):
    do_f= do_C * 1.8 +32
    return do_f
c=float(input("Nhập độ C:"))
print("Độ f tương ứng là:",chuyen_doi_nhiet_do(c))