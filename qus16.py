a=input("Enter the string:")
d={}
for i in a:
    if(i not in d):
        d[i]=a.count(i)

print(d)
