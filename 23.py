from collections import defaultdict
d,N,m=[x.split('-')for x in open('23.txt').read().split()],defaultdict(set),set()
for a,b in[*d,*[x[::-1]for x in d]]:N[a].add(b)
print(sum(any(y.startswith('t')for y in x)for x in set(tuple(sorted((x,y,z)))for x in N for y in N[x]for z in N[y]if x in N[y]and z in N[y]and x in N[z]and y in N[z]and y in N[x]and z in N[x])))
def f(R,P,X):
    global m
    if len(P)==0 and len(X)==0 and len(R)>len(m):m=R 
    for v in P:
        f(R|set([v]),P&N[v],X&N[v])
        P=P-set([v])
        X|=set([v])
f(set(),set(N),set())
print(','.join(sorted(m)))
