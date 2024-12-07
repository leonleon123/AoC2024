from functools import cache
d,f=[x.split(': ') for x in open('07.txt').read().split('\n')],cache(lambda a,t,j:a[0]==t if len(a)==1 or a[0]>t else any(f(tuple([o,*a[2:]]),t,j) for o in [a[0]+a[1],a[0]*a[1],*([int(f'{a[0]}{a[1]}')] if j else [])]))
print(*[sum(f(tuple([int(x) for x in b.split()]),int(a),j)*int(a)for a,b in d)for j in[0,1]])