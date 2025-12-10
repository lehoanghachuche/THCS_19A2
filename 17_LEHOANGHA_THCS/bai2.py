def giai_phuong_trinh_bac_nhat(a,b):
    if a==0:
        if b==0:
            print("PT vô số nghiệm")
        else:
            print("PT vô nghiệm")
    else:
        x=-b/a
        print("Kết quả là:" , x)
a=float(input("Nhập a:" ))
b=float(input("Nhập b: "))
giai_phuong_trinh_bac_nhat(a,b)
     
     