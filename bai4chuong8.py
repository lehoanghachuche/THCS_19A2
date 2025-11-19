n = int(input("Nhập n: "))
print("Số nguyên tố nhỏ hơn n: ", n )
for num in range(2,n):
    is_prime =True
    for i in range (2, int(num**0.5)):
        if num % i == 0:
            is_prime =False
            break
        if is_prime:
            print(num, end=" ")

