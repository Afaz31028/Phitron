n=int(input())
a=list(map(int,input().split()))
ok=False
cnt=0
while(ok==False):
    for i in range(0,n):
        if a[i]%2==1:
            ok=True
            break
        else:
            a[i]=a[i]//2
    cnt+=1
print(cnt-1)



