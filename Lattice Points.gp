\p 300
gsum(x,y)={a=x;m=y;s=0;k=0;\
while(m>0,\
b=a-floor(a);n=floor(m*b);tim=floor(a)*m*(m+1)/2;\
s=s+(-1)^k*(m*n+tim);k=k+1;m=n;a=1/b;);s}
gsum(2/(1+sqrt(5)),102399421*10^8)%10^8
