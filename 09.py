from numpy import array,sum,arange,multiply,where
from numpy.lib.stride_tricks import sliding_window_view as swv
d=open('09.txt').read()
dd=array([y for i, x in enumerate(d) for y in int(x)*[[i//2,-1][i%2]]])
d1,d2,idx=dd.copy(),dd.copy(),sum(dd==-1)
d1[:-idx][d1[:-idx]==-1]=d1[-idx:][d1[-idx:]!=-1][::-1]
for i in range(len(d)//2,-1,-1):
    s=d2[d2==i]
    f=where((swv(d2,len(s))==[-1]*len(s)).all(1))[0]
    if len(f) and f[0] < where(d2==i)[0][0]:d2[d2==i],d2[f[0]:f[0]+len(s)]=-1,s
print(*[int(sum(multiply(x,arange(len(x))))) for x in [d1[:-idx],d2+(d2<0)]])