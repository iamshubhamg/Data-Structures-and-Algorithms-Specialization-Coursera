#include<bits/stdc++.h>
using namespace std;
long long gcd(long long a,long long b)
{
    if(b==0)
        return a;
    long long r=a%b;
    return gcd(b,r);
}
void main()
{
    long long a,b;
    cin>>a>>b;
    cout<<gcd(a,b);
    return 0;
}
