from numpy import diff
from collections import defaultdict
d,c,mp=[int(x)for x in open('22.txt').read().split()],defaultdict(list),lambda n,s:(n^s)%16777216
def f(n,i):
    s,p=i,[i%10]
    for _ in range(n):
        s=mp(s*64,s)
        s=mp(s//32,s)
        s=mp(s*2048,s)
        p.append(s%10)
        if len(p)>5:p.pop(0)
        seq=tuple(int(x)for x in diff(p))
        if len(p)==5 and i not in[x[1]for x in c[seq]]:c[seq].append((p[-1],i))
    return s
print(sum(f(2000,x)for x in d),max(sum(x[0]for x in c[x])for x in c))