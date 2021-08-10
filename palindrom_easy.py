num=int(input("enter any num"))
rev=0
m=num
while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
if m==rev:
    print("true")
else:
    print("false")