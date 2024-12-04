from numpy import rot90, array, fliplr, diag, arange
from numpy.lib.stride_tricks import sliding_window_view as swv
d=array([[*x] for x in open('04.txt').read().split('\n')])
print(sum(y=='XMAS' or y=='SAMX' for y in [*[''.join(x) for a in [d,d.T] for x in swv(a,(1,4)).reshape(-1,4)],*[''.join(x) for a in [d,fliplr(d)] for k in range(-len(d)+4,len(d)-3) for x in swv(diag(a,k),4)]]))
print(sum(any(((x == rot90(array([*'M.S.A.M.S']).reshape((3,3)),i))==(arange(9)%2==0).reshape((3,3))).all() for i in range(4)) for x in swv(d, (3,3)).reshape(-1,3,3)))