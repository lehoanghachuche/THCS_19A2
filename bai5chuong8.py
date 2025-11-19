n = int(input("Nhập n: "))
S1 = sum(range(1, 1+n))
print("S1 = " , S1)
S2 = 1
for i in range(1,n):
    S2 *= i
    print("S2=" ,S2)
S3 = 0
for i in range(1 , 1+n):
    S3 += ((-1) **(i+1) * (i/1))
    print("S3=" ,S3)
S4 = 0
for i in range(0,i+2):
    S4 += k / (k+2)
    print ("S4=" , S4)