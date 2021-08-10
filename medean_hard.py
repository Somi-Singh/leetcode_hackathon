list1=[1,2,7]
list2=[3,5,4]
list1.extend(list2)
list1.sort()
print(list1)
i=0
count=0
sum=0
while i<len(list1):
    sum=sum+list1[i]
    count=count+1
    i=i+1
print(sum/count)

