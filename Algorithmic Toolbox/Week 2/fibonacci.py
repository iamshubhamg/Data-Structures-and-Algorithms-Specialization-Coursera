#include<bits/stdc++.h>
using namespace std;
int main()
{
    int x;
    int c=0,a=1,b=1;
    cin>>x;
        if(x==1)
            cout<<a;
        else if(x==2)
            cout<<b;
        else
        {

           for(int i=2;i<x;i++)
           {
            c=a+b;
            a=b;
            b=c;
           }
        cout<<c;
        }

    return 0;
}
