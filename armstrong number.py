num=int(input("enter a number"))
sum=0
a=num
while num>0:
    dg=num%10
    sum=sum+dg*dg*dg
    num=num//10
if a==sum:
    print("no is an armstrong number")
else:
    print("no is not an armstrong number")
