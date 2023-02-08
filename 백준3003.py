##lst = [1, 1, 2, 2, 2, 8]
##
##x = list(map(int, input().split()))
##
##print('{} {} {} {} {} {}'.format(lst[0]-x[0],lst[1]-x[1],lst[2]-x[2],lst[3]-x[3],lst[4]-x[4],lst[5]-x[5]))
a,b,c,d,e,f = map(int, input().split())

print(1-a, 1-b, 2-c, 2-d, 2-e, 8-f)
