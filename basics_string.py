a = "All apples are bad"
b = ""
for i in a.split(' '):
    i = i[0].upper()+i[1:]
    b = b+" "+i
    
print(b)
print(a.title())