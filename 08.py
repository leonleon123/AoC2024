from numpy import array, where, concat, unique
d=array([list(x) for x in open('08.txt').read().split('\n')])
f=lambda n,c:unique(concat([r[:,d[r[0,:],r[1,:]]!=y] if c else r for r,y in [(p[:,((p>=0)&(p<len(d))).all(0)],y) for p,y in [(array([((x[:,None]-x)*m+x).flatten() for x in where(d==y)]),y) for m in range(n) for y in {x for x in d.flatten() if x!='.'}]]],1),axis=1).shape[1]
print(f(3,1),f(len(d),0))