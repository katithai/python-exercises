# Viết chương trình tìm số lớn nhất trong một danh sách.
n=int(input("so mang: "))
lis=[]
for i in range(0,n):
    lis.append(input())
print(lis)

max_val = lis[0]

for i in range(1,n):
    if (lis[i] > max_val):
        max_val=lis[i]

print("value max:", max_val)