a=input("enter the string:")
choice=int(input("enter ur choice:"))
for i in a:
    if choice==1:
        prefix=input("enter the prefix:")
        if i.startsiwith(prefix):
            print("true")
        else:
            print("false")
    if choice==2:
        suffix=input("enter the suffix:")
        if i.endswith(suffix):
            print("true")
        else:
            print("false")
