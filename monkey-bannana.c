// Online C compiler to run C program online
#include <stdio.h>
int main()
{
    int n,k,j,m,p,x=0;
    scanf("%d",&n);
    scanf("%d",&k);
    scanf("%d",&j);
    scanf("%d",&m);
    scanf("%d",&p);
    if(m%k==0)
    {
        x=x+(m/k);
    }
    else
    {
        x=x+(m/k)+1;
    }
    if(p%j==0)
    {
        x=x+(p/j);
    }
    else
    {
        x=x+(p/j)+1;
    }
    printf("%d",(n-x));
}
