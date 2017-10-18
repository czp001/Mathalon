def gcd(a,b):
    if a%b==0:return b
    else:
        return gcd(b,a%b)
n,s=10**8,0
for x in range(1,int(n**0.5)+1):
    for y in range(x,int(n**0.5)+1):
        if(gcd(x,y)==1):
            s=s+int((n-0.1)/(x+y)**2)        
print s
