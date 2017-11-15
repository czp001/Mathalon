from time import clock
def mod_inv(a, p):
    b = p
    s, t = 1, 0
    while b:
      a, (q, b) = b, divmod(a, b)
      s, t = t, s - t * q
    if a != 1:
      raise ValueError("gcd(a, mod) should be 1.")
    return s if s >= 0 else s + p
def binomial_mod_pe_fast(n, m, p, e):
  def fact_valuation(n):
    n //= p
    ret = n
    while n >= p:
      n //= p
      ret += n
    return ret

  def fact_range(u, v):
    # Return the product of { up + 1, ..., up + v } modulo p^e.

    c = u % pe * p % pe
    prod = 1
    ret = 0
    for k in range(min_p_e):
      ret = (ret + prod * s1[v * min_p_e + k]) % pe
      prod = prod * c % pe
    return ret

  def cfact(n):
    # Return n! / p^{v_p(n!)} modulo p^e.

    def fact_p(u, v):
      ret = fact_range(u, v)
      if u < 2 * e - 1:
        return ret * pre[u] % pe

      # O(e)
      vs = [0] * (2 * e - 1)
      icops = [0] * (2 * e - 1)
      v, prod = 0, 1
      for i in range(2 * e - 1):
        m = u - i
        while m % p == 0:
          m //= p
          vs[i] += 1
        v += vs[i]
        icops[i] = prod
        prod = prod * m % pe

      # O(e log(p))
      iprod = mod_inv(prod, pe)
      for i in range(2 * e - 2, -1, -1):
        icops[i] = iprod * icops[i] % pe
        iprod = iprod * ((u - i) // pows[vs[i]]) % pe

      # O(e)
      s = 0
      for i in range(2 * e - 1):
        j = 2 * e - 2 - i
        ex = v - vs[i] - cfac_vs[j] - cfac_vs[i]
        if ex >= e:
          continue
        denom = cifac[j] * cifac[i] % pe
        if j & 1:
          denom = pe - denom
        t = pows[ex] * prod % pe * icops[i] % pe * denom % pe * pre[i] % pe
        s = (s + t) % pe
      assert(s % p != 0)
      ret = ret * s % pe
      return ret

    # O(e log(p))
    ret = 1
    fac_ex = 0
    while n > 0:
      q, v = divmod(n, p)
      u = q % period
      fac_ex += u
      ret = ret * fact_p(u, v) % pe
      n = q
    ret = ret * pow(fac, fac_ex % period, pe) % pe
    return ret

  if p <= 1:
    raise ValueError("p should be prime." % p)

  if m < 0 or n < m:
    return 0
  
  needed_e = e - (fact_valuation(n) - fact_valuation(m) - fact_valuation(n - m))
  if needed_e <= 0:
    return 0

  ret = p ** (e - needed_e)

  e = needed_e
  pe = p ** e
  period = 2 * pe // p
  if p == 2 and e >= 3:
    period = period // 2
  pows = [1] * e
  for i in range(1, e):
    pows[i] = pows[i - 1] * p

  # stirling 1: O(p * min(p, e))
  min_p_e = min(p, e)
  s1 = [0] * (p * min_p_e)
  s1[0] = 1
  for k in range(1, p):
    o = k * min_p_e
    s1[o] = s1[o - min_p_e] * k % pe
    for i in range(1, min_p_e):
      s1[o + i] = (s1[o + i - min_p_e - 1] + s1[o + i - min_p_e] * k) % pe

  # ((kn)!)_p / ((n!)_p)^k: O(e * min(p, e) + e log(p))
  fac = fact_range(0, p - 1)
  ifac = mod_inv(fac, pe)
  pre = [1] * (2 * e - 1)
  for i in range(1, 2 * e - 1):
    pre[i] = pre[i - 1] * fact_range(i - 1, p - 1) % pe * ifac % pe

  # (coprime?) factorials: O(e + e log(p))
  cifac, cfac_vs = [1] * (2 * e - 1), [0] * (2 * e - 1)
  prod = 1
  for i in range(1, 2 * e - 1):
    j, v = i, 0
    while j % p == 0:
      j //= p
      v += 1
    cfac_vs[i] = cfac_vs[i - 1] + v
    prod = prod * j % pe
    cifac[i - 1] = j
  cifac[-1] = mod_inv(prod, pe)
  for i in range(2 * e - 3, -1, -1):
    cifac[i] = cifac[i + 1] * cifac[i] % pe

  numer = cfact(n)
  denom = cfact(m) * cfact(n - m) % pe
  return (numer % pe * mod_inv(denom, pe) % pe) * ret

def factor(n):
    if n in [-1, 0, 1]: return []
    if n < 0: n = -n
    F = []
    while n != 1:
        p = trial_division(n)
        e = 1
        n //= p
        while n%p == 0:
            e += 1; n //= p
        F.append([p,e])
    F.sort()
    return F

def trial_division(n, bound=None):
    if n == 1: return 1
    for p in [2, 3, 5]:
        if n%p == 0: return p
    if bound == None: bound = n
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7; i = 1
    while m <= bound and m*m <= n:
        if n%m == 0:
            return m
        m += dif[i%8]
        i += 1
    return n

def solve(n):
    s=0
    f=factor(n)
    for i in f:
        m=n//i[0]**i[1]
        s=s+binomial_mod_pe_fast(10**18, 10**10, i[0], i[1])*m*mod_inv(m,i[0]**i[1])
    s=s%n
    return s

start=clock()
ans=0
for i in range(2,200000):
    ans=ans+solve(i)
print(ans)
print(clock()-start,'secs')
