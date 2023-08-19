a =4452
# if a is divisible by 10 and a is divisible 50
# a should not be 100
#or 

# if a is divisible by 5 then print
# and 
# a should not divisible by 20

if [a%10 ==0 and a%50 ==0 and a ==100] or [a%5==0 and a%20 !=0]:
    print("-print")
else:
    print("-not print")

print("-print") if [a%10 ==0 and a%50 ==0 and a ==100] or [a%5==0 and a%20 !=0] else print("-not print")



if a%10 ==0:
    if a%50 ==0:
        if  a%100 !=0:
            print("--print")
else:
    print("--not print")    