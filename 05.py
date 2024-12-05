import re
from functools import cmp_to_key
r,d=[[re.split(r',|\|',y) for y in x.split('\n')] for x in open('05.txt').read().split('\n\n')]
df=[(x,sorted(x,key=cmp_to_key(lambda a,b: 1-2*any(c==a and d==b for c,d in r)))) for x in d]
print(sum(int(x[len(x)//2])*(x==xs) for x,xs in df),sum(int(xs[len(xs)//2])*(x!=xs) for x,xs in df))