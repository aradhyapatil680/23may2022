minus=lambda a,b:a-b
print(minus(5,3))

sqr=lambda c : c*c
print(sqr(8))

a=[[1,4],[2,6],[5,1],[6,7]]
a.sort(key=lambda x:x[1])
print(a)