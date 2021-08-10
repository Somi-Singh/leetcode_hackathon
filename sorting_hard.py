a=[[1,4,5],[1,3,4],[2,6]]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        b.append(a[i][j])
        j+=1
    i+=1
index=0
while index<len(b):
    k=0
    while k<len(b)-1:
        if b[k]>b[k+1]:
            b[k],b[k+1]=b[k+1],b[k]
        k+=1
    index+=1
print(b)