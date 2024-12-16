from numpy import array, where
from functools import reduce
d=array([[*x]for x in open('16.txt').read().split('\n')])
S,E=[tuple(int(x)for x in array(where(d==x)).flatten())for x in'SE']
paths,q,v=[],[(0,tuple(S),0,set([S]))],{}
while len(q):
    s,p,dr,path=q.pop(0)
    if p==E: paths.append((s,path))
    if(p,dr)in v and v[(p,dr)]<s or p==E: continue
    v[(p,dr)],x=s,[(0,1),(1,0),(0,-1),(-1,0)][dr]
    pp = (p[0]+x[0],p[1]+x[1])
    if d[pp] in '.E': q.append((s+1,pp,dr,path|set([pp])))
    q.append((s+1000,p,(dr+1)%4,path))
    q.append((s+1000,p,(dr-1)%4,path))
t=min(paths,key=lambda x:x[0])[0]
print(t,len(reduce(lambda a,b:a|b,[path for dst,path in paths if dst==t],set())))