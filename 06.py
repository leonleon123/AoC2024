from numpy import array, where
d=array([list(x) for x in open('06.txt').read().split('\n')])
def find_path(d):
    p,ds,di,v=array(where(d=='^')).T[0],[(-1,0),(0,1),(1,0),(0,-1)],0,set()
    while '#'in(line:={(-1,0):d[:p[0],p[1]][::-1],(0,1):d[p[0],p[1]+1:],(1,0):d[p[0]+1:,p[1]],(0,-1):d[p[0],:p[1]][::-1]}[ds[di]]):
        n=where(line=='#')[0][0]
        if(s:={(p[0]+ds[di][0]*i,p[1]+ds[di][1]*i,ds[di]) for i in range(n+1)}).issubset(v):return v,1
        p,di,v=(p[0]+ds[di][0]*n,p[1]+ds[di][1]*n),(di+1)%4,v|s
    v|={(p[0]+ds[di][0]*i,p[1]+ds[di][1]*i,ds[di]) for i in range(len(line)+1)}
    return v,0
def place(d,p):
    dc=d.copy()
    if dc[p[0],p[1]]!='^': dc[p[0],p[1]]='#'
    return dc
print(len((l:=set([(x[0],x[1]) for x in find_path(d)[0]]))),sum(find_path(place(d,p))[1] for p in l))