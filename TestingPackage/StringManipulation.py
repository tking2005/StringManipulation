mystring="Apple"
count=len(mystring)
print(count)
for a in range (0,count):
    print(mystring[a])

c=0
while c<count:
    print(mystring[c],end="")
    c+=1
lowermystring=mystring.lower()
uppermystring=mystring.upper()
print("")
print(lowermystring)
print(uppermystring)
whitespacestring="        A p p l e     "
print (whitespacestring)
whitespacestring=whitespacestring.strip()
print(whitespacestring)
whitespacestring=whitespacestring.split()
print(whitespacestring)
