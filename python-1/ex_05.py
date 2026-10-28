lis1=[23, 65, 19, 90]
print("Các chỉ số để hoán đổi:")
n=int(input())
m=int(input())
lis1[n], lis1[m] = lis1[m], lis1[n]
print(lis1)
