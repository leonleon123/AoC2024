from numpy import array, where
from itertools import permutations
from functools import cache
d=open('21.txt').read().split()
pads = {
    'n': array(list('789456123 0A')).reshape(4,3),
    'd': array(list(' ^A<v>')).reshape(2,3)
}
dirs = {'<':(0,-1),'>':(0,1),'^':(-1,0),'v':(1,0)}

def is_valid_path(path, pad_id, p):
    b = (0,0) if pad_id == 'd' else (3,0)
    for c in path:
        p = (p[0] + dirs[c][0], p[1] + dirs[c][1])
        if p == b: return False
    return True

@cache
def segment(a, b, pad_id):
    (ai, aj),(bi, bj)=[array(where(pads[pad_id]==x)).flatten() for x in[a,b]]
    di,dj=bi-ai,bj-aj
    return set(''.join(path)+'A' for path in permutations(('>'if dj>=0 else'<')*abs(dj)+('v'if di>=0 else'^')*abs(di)) if is_valid_path(path,pad_id,(ai,aj))) or set('A')

@cache
def length(code, depth, pad_id):
    return len(code) if depth==0 else sum(min(length(x,depth-1,'d') for x in segment(code[i],code[i+1],pad_id)) for i in range(-1,len(code)-1))

print(*[sum(length(code,x+1,'n') * int(code[:-1]) for code in d) for x in [2,25]])