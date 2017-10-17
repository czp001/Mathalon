#include <iostream>
#include<cmath>
#include<cstdio>
#include<ctime>
using namespace std;

int p[50]={2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,199,211, 223, 227, 229};
int po(int n,int m,int p)
{
    int s=0;
    int t=p;
    for(int i=1;i<=15;i++)
    {
        s=s+n/t-m/t-(n-m)/t;
        t=t*p;
        if(t>n)break;
    }
    return s;
}
int sq(int n,int m)
{
    int k=(int)sqrt(n);
    bool flag=1;
    int i=0;
    while(p[i]<=k)
    {
        if(po(n,m,p[i])>=2)
        {
            flag=0;
            break;
        }
        i++;
    }
    return flag;
}
int f(int n)
{
    int s=0;
    for(int i=0;i<=n;i++)
    {
        if(sq(n,i))s=s+1;
    }
    return s;
}
int main()
{
    int M=0;
    clock_t s=clock();
    for(int i=1;i<=40000;i++)
    {
        int s=f(i);
        if(s>M)
        {
            M=s;
            printf("%d,%d\n",i,M);
        }
    }
    printf("%f\n",(clock()-s)*1.0/CLOCKS_PER_SEC);
    return 0;
}
