a(n)=bittest(n, 0) && return(n==1); my(P=1); n && !for(i=2, #n=factor(n)~, n[1, i]>1+(P*=sigma(n[1, i-1]^n[2, i-1])) && return)
t=0;s=0;for(n=10^18,10^18+10^4,if(a(n),t++;s=s+n));[t,s%10^18]
