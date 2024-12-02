from numpy import logical_and, diff, delete
print(*[sum(any((all(x>=0) or all(x<=0)) and all(logical_and(abs(x)>=1,abs(x)<=3)) for x in [diff(delete(y,i) if p else y) for i in range(len(y))]) for y in [[int(y) for y in x.split(' ')] for x in open('02.txt').read().split('\n')]) for p in [0,1]])
