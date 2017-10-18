from time import clock
start=clock()
a=[0]*1000
def f(n):
    s=str(n)
    l=len(s)
    f=0
    for i in range(l):
        a[i]=int(s[i])
    i=l
    a[i]=sum(a[i-l:i])
    while(a[i]<=n):
        if a[i]==n:
            f=1
            break
        i=i+1
        a[i]=sum(a[i-l:i])
    return f

s=[]
for i in range(10**7,10**8+1):
    if(f(i)):s=s+[i]
print s
print clock()-start,'secs'
