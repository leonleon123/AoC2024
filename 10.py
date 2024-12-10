from numpy import array, where
from functools import reduce
d=array([list(x) for x in open('10.txt').read().split('\n')])
s=[tuple(x) for x in zip(*where(d=='0'))]
g=lambda p,r,f:r(p)if d[p]=='9' else f(g(x,r,f) for x in [(p[0]+1,p[1]),(p[0]-1,p[1]),(p[0],p[1]+1),(p[0],p[1]-1)] if x[0]>=0 and x[1]>=0 and x[0]<len(d) and x[1]<len(d) and d[x]!='.' and int(d[x])==int(d[p])+1)
print(sum(len(g(x,lambda x:set([x]),lambda a:reduce(lambda c,d:c|d,a,set()))) for x in s),sum(g(x,lambda a:1,sum) for x in s))