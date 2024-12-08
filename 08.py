from numpy import array, where, sum
d=array([list(x) for x in open('08.txt').read().split('\n')])
def f(n):
    o=d.copy()
    for y in {x for x in d.flatten() if x!='.'}:
        c=where(d==y)
        for m in range(2,n+1):
            p=array([((x[:,None]-x)*m+x).flatten() for x in c]).T
            for i,j in p[((p>=0)&(p<len(o))).all(axis=1)].reshape(-1,2): 
                if d[i,j]!=y:o[i,j]='#'
    return o
print(sum(f(2)=='#'),sum(f(len(d))!='.'))