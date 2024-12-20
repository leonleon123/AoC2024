from numpy import array,where,sum
from collections import defaultdict
d=array([list(x)for x in open('20.txt').read().split('\n')])
S=tuple(int(x)for x in array(where(d=='S')).flatten())
l,q,m={S: 0},[(0,S,set([S]))],sum(d=='.')+1
while len(q)<=m:
    t,p,v=q[-1]
    for pp in [(p[0]+i[0],p[1]+i[1])for i in[(0,1),(1,0),(0,-1),(-1,0)]]:
        if pp not in v and d[pp]!='#':q,l[pp]=q+[(t+1,pp,v|{pp})],t+1
def f(n):
    c=defaultdict(int)
    for _,p,_ in q:
        a=array(where((d=='.')|(d=='E'))).T
        x=sum(abs(a-p),axis=1)
        for e,i in zip([tuple(x)for x in a[x<=n,:]],x[x<=n]):c[l[p]+i+(m-l[e])]+=1
    return sum([c[x]for x in c if m-x>=100])
print(f(2),f(20))
