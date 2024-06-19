a=input("Enter string1: ")
b=input("Enter string2: ")
d1={}
d2={}
for i in a:
    if i not in d1:
        d1[i]=a.count(i)

for j in b:
    if j not in d2:
        d2[j]=b.count(j)

print(d1)
print(d2)
print(d1==d2)

if (d1==d2):
    print("The strings are anagrams of each other")
else:
    print("They are not anagrams")

