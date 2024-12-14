from numpy import array, zeros
from math import prod
d,m,n=array([tuple(int(y)for y in x[2:].split(','))for x in open('14.txt').read().split()]).reshape(-1,4),101,103
f,i=zeros((m,n)),0
while'#'*33 not in'\n'.join(''.join('.#'[int(y)]for y in x)for x in f):
    f[:],d[:,0:2],i=0,(d[:,0:2]+d[:,2:4])%[m,n],i+1
    if i==100:print(prod(sum(((d[:,0:2][(d[:,0:2]!=[m//2,n//2]).all(1),:]<[m//2,n//2])@[2,1])==x)for x in range(4)))
    f[d[:,0],d[:,1]]=1
print(i)