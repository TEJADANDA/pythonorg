dict_a={'name':'teja','age':'15'}
dict_a['name']='hari'
print(dict_a)
del dict_a['age']
print(dict_a)

dict_a={m:m**2 for m in range(8)}
print(dict_a)

n=int(input("enter"))
i=1
for j in range(1,n+1):
    while(i<=n+1):
        if(i**2==j):
            print(j)
    i=i+1

