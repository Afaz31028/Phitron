s=input()
c=0
d=0
k=0
l=0
box=[]
n=len(s)
for i in range(0,n):
    if s[i]=='L':
        c=c+1
    else:
        d=d+1
    k=k+1
    if c==d and c>0 and d>0:
        box.append(l)
        box.append(k-1)
        i=0
        j=0
        l=k
m=len(box)
print(m//2)
z=0
for i in range(0,m//2):
    p=box[z]
    q=box[z+1]
    z=z+2
    for j in range(p,q+1):
        print(s[j],end="")
    print("")







