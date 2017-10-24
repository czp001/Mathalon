''' At first,use Mathematica to get 10^7 digits of Pi,and save in pi.txt,takes 33 secs
Export["pi.txt", 
 StringJoin[
  ToString /@ (RealDigits[\[Pi], 10, 10^7 + 1] // First // 
     Drop[#, 1] &)]]
'''     
#Than use manacher algorithms,takes 3 secs

import os
from time import clock

def manacher(s):
    s='#'+'#'.join(s)+'#'
    RL=[0]*len(s)
    MaxRight=0
    pos=0
    MaxLen=0
    for i in range(len(s)):
        if i<MaxRight:
            RL[i]=min(RL[2*pos-i], MaxRight-i)
        else:
            RL[i]=1
        while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
            RL[i]+=1
        if RL[i]+i-1>MaxRight:
            MaxRight=RL[i]+i-1
            pos=i
        MaxLen=max(MaxLen, RL[i])
    return MaxLen-1
    
def huiwen(l):
	return l==l[::-1]
    
start=clock()
f=open('pi.txt')
pi=f.readline()
ml=manacher(pi)
print 'max length: ',manacher(pi)
for i in range(10**7):
	s=pi[i:i+ml]
	if huiwen(s):
		print "%s,%d"%(s,i)
		break
print clock()-start,'secs'
