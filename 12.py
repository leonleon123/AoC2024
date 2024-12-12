from numpy import array, sort, diff
from functools import reduce
from collections import defaultdict
d,v=array([[*x]for x in open('12.txt').read().split('\n')]),set()
b=lambda x:x[0]>=0 and x[1]>=0 and x[0]<d.shape[0] and x[1]<d.shape[1]
n=lambda x:[(x[0]+1,x[1]),(x[0]-1,x[1]),(x[0],x[1]+1),(x[0],x[1]-1)]
g=lambda p,c:(v.add(p) or 1) and reduce(lambda a,b:a|b,[g(x,d[x])for x in n(p)if b(x)and x not in v and d[x]==c],set([p]))
p=lambda g:sum(sum(y not in g for y in n(x))for x in g)*len(g)
def s(g):
    s=defaultdict(list)
    for x in g:
        for i, y in enumerate(n(x)):y not in g and s[(x[i>=2],i)].append(x)
    return sum(sum(diff(sort(array(s[x])[:,int(not(x[1]//2))]))>1)+1 for x in s)*len(g)
t=[g((i,j),d[i,j])for i in range(d.shape[0])for j in range(d.shape[1])if not(i,j)in v]
print(*[sum(f(x)for x in t)for f in[p,s]])