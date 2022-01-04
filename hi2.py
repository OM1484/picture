def countwords():
    name=input("enter file name ")
    file=open(name, "r")
    number=0
    for i in file:
        words=i.split()
        number=number+len(words)
    print(number)

countwords()