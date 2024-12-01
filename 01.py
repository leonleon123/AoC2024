d=[*map(int,open("01.txt").read().split())]
print(sum(abs(a-b) for a,b in zip(sorted(d[::2]),sorted(d[1::2]))),sum(x*d[1::2].count(x) for x in d[::2]))