a=int(input("Enter the operation you want to do: 1 for + \n 2 for - \n 3 for * \n 4 for division:"))
b=int(input("Enter the first number:"))
c=int(input("Enter the second number:"))
if a==1:
    print("The sum of given two number is:", b+c)
elif a==2:
    print("The difference of the given two number number is:",b-c)
elif a==3:
    print("The multiplication fo the given numbers is: ",b*c)
elif a==4:
    print("The divison of the given numbers is: ",a/b)
else:
    print("please enter a valid number")
