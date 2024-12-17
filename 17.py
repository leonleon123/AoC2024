from re import findall
from numpy import split

r,p=split([int(x) for x in findall(r'\d+',open('17.txt').read())],[3])

def run(r,p,a=r[0]):
    r=r.copy()
    r[0],i,o=a,0,[]
    while i<len(p):
        c=p[i+1]if p[i+1]>=0 and p[i+1]<=3 else r[p[i+1]-4]
        if p[i]==0:r[0]=r[0]>>c
        elif p[i]==1:r[1]=r[1]^p[i+1]
        elif p[i]==2:r[1]=c%8
        elif p[i]==3:
            if r[0]!=0:i=p[i+1]-2
        elif p[i]==4:r[1]=r[1]^r[2]
        elif p[i]==5:o.append(c%8)
        elif p[i]==6:r[1]=r[0]>>c
        elif p[i]==7:r[2]=r[0]>>c
        i+=2
    return o

def to_int(g):
    return int(''.join([bin(x)[2:].zfill(3)for x in g]),2)

def find(idx,g):
    if idx<0:return to_int(g)
    for i in range(8):
        g[len(p)-idx-1]=i
        o=run(r,p,to_int(g))
        if len(o)==len(p)and o[idx]==p[idx]:
            b=find(idx-1,g)
            if b>0:return b
    return -1

print(','.join([str(x) for x in run(r,p)]),find(len(p)-1,[7]*len(p)))