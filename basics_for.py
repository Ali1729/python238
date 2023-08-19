# 

# a = list(range(10))
# b = list(range(10))

# print(a[2])
# print(a[4])
# print(a[6])
# print(a)
# print(b)

# for (i =0;i<len(a);i++):
#     if i%2 ==0:
#         print(a[i])

# for i in a:
#     # for loop accepts an iterator
#     # i is the actual value.
#     # a is list here.. and list supports iterator
#     print(i)
    

for i in a:
    for j in b:
        print(i,j)

# a = [[1,2],[3,4],[5,6]]
# for i,j in a:
#     print(i,j)
    
# a = [[1,2],[3,4],[5,6]]
# for i in a:
#     print(i[0],i[1])
    


a = list(range(10))
b = list(range(10))    
c = list(range(10))    

for i,j,k in zip(a,b,c):
    print(i,j)