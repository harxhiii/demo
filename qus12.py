a=int(input("Enter a number: "))
sum=0
while a>0:
    n=a%10
    sum+=n
    a=int(a/10)

print("the sum of the digits of the given number is: ",sum)

