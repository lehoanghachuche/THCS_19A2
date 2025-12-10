def kiem_tra_so_doi_xung(n):
    dao = 0
    temp = n
    while temp > 0:
        dao = dao * 10 + temp % 10
        temp //= 10
    return dao == n
n = int(input("Nhập số n: "))
print(kiem_tra_so_doi_xung(n))