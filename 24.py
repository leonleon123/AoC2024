from re import findall
a,b=open('24.txt').read().split('\n\n')
d={x:int(y)for x, y in findall(r"(.*): (1|0)",a)}
p={d:(a,b,c)for a,b,c,d in findall(r"(.*) (AND|OR|XOR) (.*) -> (.*)",b)}
func={"AND":lambda a,b:a&b,"OR":lambda a,b:a|b,"XOR":lambda a,b:a^b}
compute=lambda o:d[o]if o not in p else func[p[o][1]](compute(p[o][0]),compute(p[o][2]))
print(int(''.join(str(x[1])for x in sorted((x,compute(x))for x in p if x.startswith('z'))[::-1]),2))