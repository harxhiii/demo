tem=float(input("ENTER THE TEMPERATURE:"))
ch=int(input("ENTER UR CHOICE:"))
result=0
print("1.celsius to farenhite 2.farehite to celsius")
if ch==2:
    result=(tem-32)*5/9
    print("farehhite to celsius:",result)
if ch==1:
    result=(tem*9/5)+32
    print("cesius to farehntie:",result)

