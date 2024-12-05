from collections import Counter
n=int(input())
y=list(map(int,input().split()))
num=Counter(y)
cnt=0
for key,val in num.items():
    if val<key:
        cnt=cnt+val                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    elif val>key :
        cnt=cnt+(val-key)
print(cnt)
# seq={}
# for val in y:
#     seq[val]+=1

# for key, val in seq.items():
#     print(key,val)