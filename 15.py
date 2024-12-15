from numpy import array,where,sum
a,b=open('15.txt').read().split('\n\n')
def affected_1(p,x,v,d):
    n=(p[0]+x[0],p[1]+x[1])
    return affected_1(n,x,v|set([p]),d)if d[n]=='O'else(v|set([p]),d[n]=='.')
def affected_2(p,x,v,d):
    n=(p[0]+x[0],p[1]+x[1])
    if d[n]in'[]':
        if x[0] != 0:
            lv,l=affected_2((n[0],n[1]-1+2*(d[n]!=']')),x,v|set([p]),d)
            rv,r=affected_2(n,x,v|set([p]),d)
            return (lv|rv,l&r)
        return affected_2(n,x,v|set([p]),d)
    return (v|set([p]),d[n]=='.')
def move(d,f):
    p=tuple(array(where(d=='@')).flatten())
    for x in[{'^':(-1,0),'>':(0,1),'v':(1,0),'<':(0,-1)}[x]for x in b if x!='\n']:
        i,e=f(p,x,set(),d)
        if e:
            idx=array([*i])
            t=d[idx[:,0],idx[:,1]]
            d[idx[:,0],idx[:,1]]='.'
            d[idx[:,0]+x[0],idx[:,1]+x[1]]=t
            p=(p[0]+x[0],p[1]+x[1])
    return d
print(*[sum(array(where(x)).T*[100,1]) for x in [move(array([[*x] for x in a.split('\n')]),affected_1)=='O',move(array([[*x.replace('#','##').replace('O','[]').replace('.','..').replace('@','@.')] for x in a.split('\n')]),affected_2)=='[']])