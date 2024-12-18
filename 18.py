from numpy import array,inf
from re import findall
from heapq import heappop,heappush
from collections import defaultdict

d=array(findall(r"\d+",open('18.txt').read())).reshape(-1,2).astype(int)

def shortest_path(a):
    c,s,m,n,h=set([tuple([int(x[1]),int(x[0])]) for x in d[:a]]),defaultdict(lambda:inf),71,71,[(0,(0,0))]
    while len(h):
        t,p=heappop(h)
        if t>s[p]:continue
        for i in [(1,0),(-1,0),(0,1),(0,-1)]:
            pp=(p[0]+i[0],p[1]+i[1])
            if pp[0]<0 or pp[1]<0 or pp[0]>=m or pp[1]>=n:continue
            if pp in c:continue
            if t+1<s[pp]:
                s[pp]=t+1
                heappush(h,(t+1,pp))
    return s[(m-1,n-1)]

def find_blocking():
    i,o=1,-1
    while o!=inf:
        o=shortest_path(i)
        i+=1
    return','.join([str(x) for x in d[i-2]])

print(shortest_path(1024),find_blocking())