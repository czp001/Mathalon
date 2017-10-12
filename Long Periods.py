#not finish yet
from math import log
from time import clock
start=clock()
def p(n):
    cf=0
    s=int(n**0.5)
    m0,d0,a0=0,1,s
    m1=d0*a0-m0
    d1=(n-m1*m1)//d0
    a1=(s+m1)//d1
    cf+=1
    while a1!=2*s:
        m0,d0,a0=m1,d1,a1
        m1=d0*a0-m0
        d1=(n-m1*m1)//d0
        a1=(s+m1)//d1
        cf+=1
    return cf
    
print p(61)

def f(d):
    if d%8==1:
        return d**0.5*log(log(d))
    else:
        return d**0.5*log(log(4*d))

m=0
D=101
for d in range(102,5*10**7):
    if d!=(int(d**0.5))**2:
        M=p(d)/f(d)
        if M>m:
            m=M
            D=d
    if d%10000000==0:print d,clock()-start,'secs'
print D,M
print clock()-start,'secs'
