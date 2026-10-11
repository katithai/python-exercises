# Viết chương trình kiểm tra xem một số có phải là số nguyên tố hay không.
n=int(input("số : " ))
print(n)
if n < 2:
    print("không phải số nguyên tố")
else:
    for i in range(2, n):
        if n % i == 0:
            print("không phải số nguyên tố")
            break
    else:
        print("là số nguyên tố")