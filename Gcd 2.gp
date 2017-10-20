pow(p)=sum(i=1,20,1162261467\p^i)
f(p)=t=0;while(Mod(2,p^(t+1))^1162261467-1==0,t++);t
s=1;t=0;forprime(p=2,1162261467,s=s*p^min(f(p),pow(p));t++;if(t%10^6==0,print(t)));s
