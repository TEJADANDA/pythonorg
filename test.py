m=4
n=5
m=str(m)
l=m*n
print(list(l))
n=int(input("enter a number"))
print(n)
a="apple"
b="application"
print(list(a))
print(list(b))
print(a[:2]==b[:2])
x='943'
z='748'
print(x<z)
n1=input()
n2=input()
print(n1[0]<n2[:-1])
a=[]
a.append(1,2,3,4)
print(a)
print((2<3) and (3<2))
m=int(input())
p=int(input())
c=int(input())
print((m>=70 and p>=60 and c>=60))
print(m+p+c>=180)
a="PyTHon"
print(a.swapcase())
#replace
a="dd-mm-yy"
print(a.replace("-","/"))
a="madax"
print(a[::-1]==a)
a="mA@2"
print(a[::1==a.isupper()] and a[::1==a.islower()] and a[::1==int()])
name=input()
teja=0
surya=0
hari=0
suma=0
for i in range(len(name)):
    if(name[i].isupper()):
        teja+=1
    if(name[i].islower()):
        surya+=1
    if(name[i].isdigit()):
        hari+=1
    if(name[i]=="@"):
        suma+=1
if(teja==1 & surya==1 & hari==1 & suma==1):
    print("it is astrong password")
else:
    print("no")
l=input()
print(l.isupper())
l="lAshs"
print(l[::-1].isupper())
lop=input()
print(lop[-1])
set_a = surya
print(set_a)
list_a = [1,2,2,3,4,5,6]
for i in range(len(list_a)):
    if(list_a[::1]==list_a[::-1]):
        print(list_a.remove)
    else:
        print(\)
list_b=[1,2,3,4,4,5,5]
set_a=set(list_b)
print(set_a)
set_a=list(set_a)
print(set_a)
list_z=[1,2,6,7,8,9]
set_a={1,3,5,4,7,8}
set_b={1,3,6,8,5,7}
print(set_a & set_b)
list_y=input()
list_y=[1,2,"&",5,"*","#"]
set_a={1,2,3,4,5,6,7}
set_b={2,3,5,7,3,5}
set_c={4,5,6,83,5,5}
print(set_a & set_b & set_c)
list_a=["@","#",1]
list_b=list_a.copy()
for i in range(len(list_a)):
    if str(list_a[i].isdigit()):
        print(list_a)
    else:
        list_b.remove(list_a)
    print(list_b)
set_a={1,2,3,4,5,6}
set_b={1,3,5,6}
print(set_b.issubset(set_a))
set_a={1,2,3,4,5,6}
set_b={1,3,5,6}
print(set_a.issuperset(set_b))
set_a={1,3,2,2,2}
set_b={9,7,8,7}
print(set_a.isdisjoint(set_b))
list_a=[1,2,3,4,5,6,7,8]
list_b=list_a.copy()
list_c=[]
k=int(input("enter"))
for i in range(len(list_a)):
    for j in range(len(list_b)):
        if(list_a[i]+list_b[j] == k):
            print(list_a[i], list_b[j])
            list_c=[list_a[i],list_b[j]]
            list_b.append(list_c)
print(list_b)

dict_a={'name':'teja','age':'15'}
dict_a['name']='hari'
print(dict_a)


