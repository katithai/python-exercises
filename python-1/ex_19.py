t1 = (1, 2, 3, 4, 5, 6)
t2 = (4, 5, 6, 7, 8, 9)
lis=[]
for x in range(0,len(t1)):
    if t1[x] in t2:
        lis.append(t1[x])

print("Common elements:",  lis)