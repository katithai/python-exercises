a= [1, 5, 10, 20]
b=[6, 10, 20, 80, 100]
c=[3, 10, 15, 20, 30, 70, 80]

for i in   range(0,len(a)):
    if(a[i] in b ):
        if(a[i] in c ):
            print(a[i])
