from re import findall
d=[[int(b)for _,b in findall(r'(\+|=)(\d+)',x)]for x in open('13.txt').read().split('\n\n')]
print(*[int(sum((y*3+x)*((x%1)+(y%1)==0)for x,y in[((a*(f+g)-(c+g)*d)/(e*a-b*d),(e*(c+g)-b*(f+g))/(e*a-b*d))for a,d,b,e,c,f in d]))for g in[0,10**13]])