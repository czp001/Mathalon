MOD=1000000007
N=60

inv=[0]*(N+2)
inv[1]=1
for i in range(2,N+2):
    inv[i] = MOD - ((MOD//i * inv[MOD%i] % MOD))
    
C = [[0 for col in range(N+2)] for row in range(N+1)]
C[0][1]=1
for k in range(1,N+1):
    s=1
    for i in range(k+1,1,-1):
        C[k][i]=k*inv[i]*C[k-1][i-1]%MOD
        s=(s-C[k][i])%MOD
    C[k][1]=s
    
def S(n,m):
    s=0
    t=1
    for i in range(1,m+2):
        t=t*n%MOD
        s=(s+t*C[m][i])%MOD
    return s

def D(n,k):
    s = 0
    u = int(n ** 0.5)
    for i in range(1, n // (u + 1) + 1):
        s = s + i ** k * (n // i)
    for d in range(1, u + 1):
        s = s + S(n // d, k)
    s = s - u * S(n // (u + 1), k)
    return s

print D(10**15,13)%MOD
