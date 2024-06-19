lst=[]
n=int(input("enter number of elements"))
sum=0
for i in range(n):
    ele=int(input())
    lst.append(ele)
    print(lst)
for i in lst:
    sum=sum+i
    print(sum)
