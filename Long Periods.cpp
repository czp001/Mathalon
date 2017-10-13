#include<cstdio>
#include<cmath>
#include<ctime>
using namespace std;

int p(int n)
{
    int cf=0;
	int s=sqrt(n);
	int m0=0;
	int d0=1;
    int a0=s;
    int m1=d0*a0-m0;
    int d1=(n-m1*m1)/d0;
    int a1=(s+m1)/d1;
    cf+=1;
    while(a1!=2*s)
    {
	m0=m1;
	d0=d1;
	a0=a1;
	m1=d0*a0-m0;
        d1=(n-m1*m1)/d0;
        a1=(s+m1)/d1;
        cf+=1;
	}
    return cf;
}

float f(int d)
{
    if(d%8==1)return sqrt(d)*log(log(d));
    return sqrt(d)*log(log(4*d));
}

int main()
{
	clock_t s=clock();
	float M,m=0;
	int D=101;
    for(int d=102;d<500000000;d++)
    {
		if(d!=((int) sqrt(d))*((int) sqrt(d)))
		{
	    	M=p(d)/f(d);
	    	if(M>m){m=M;D=d;}
		}
		if(d%1000000==0)printf("%d:%d,%f,%f\n",d,D,m,(clock()-s)*1.0/CLOCKS_PER_SEC);
    }
    printf("%d,%f\n",D,M);
	printf("%f\n",(clock()-s)*1.0/CLOCKS_PER_SEC);
    return 0;
}
