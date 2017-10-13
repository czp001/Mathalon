f(n)=s=0;for(i=0,n,if(issquarefree(binomial(n,i)),s++));s
m=0;n0=0;for(i=1,40000,c=f(i);if(c>m,n0=i;m=c));[n0,m]
