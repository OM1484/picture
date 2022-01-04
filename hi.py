intro=input("Enter about your self ")
words=1
letters=0
for i in intro:
    letters=letters+1
    if i==" ":
        words=words+1
        letters=letters-1
print(words)
print(letters)

