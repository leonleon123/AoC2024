from re import split
from functools import cache
a,b=[split(r"\n|, ",x)for x in open('19.txt').read().split('\n\n')]
f=cache(lambda t:1 if t==''else sum(f(t[len(x):])for x in a if t.startswith(x)))
print(sum(f(x)>0 for x in b),sum(f(x)for x in b))