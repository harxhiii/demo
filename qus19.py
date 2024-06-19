a=input("enter the string: ")
l=[".",",","?","!",":",";","[","]","{","}","(",")","'"]
for i in a:
    if i in l:
        continue

    else:
        print(i,end='')
