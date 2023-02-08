a,b,c = map(int,input().split())

aa=a*b//c
bb=a//b*c
cc=a*c//b

print(max(aa,bb,cc))
