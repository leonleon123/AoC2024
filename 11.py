from collections import defaultdict
from math import log,floor
d=defaultdict(int,{int(x):1 for x in open('11.txt').read().split()})
def blink(n,c=d.copy()):
    for t in [defaultdict(int)for _ in range(n)]:
        for x in c:
            m=floor(log(x,10))+1 if x!=0 else 1
            if x==0:t[1]+=c[x]
            elif x!=1 and m%2==0:
                t[x//10**(m//2)]+=c[x]
                t[x%10**(m//2)]+=c[x]
            else:t[x*2024]+=c[x]
        c=t
    return sum(c.values())
print(*[blink(x) for x in [25,75]])