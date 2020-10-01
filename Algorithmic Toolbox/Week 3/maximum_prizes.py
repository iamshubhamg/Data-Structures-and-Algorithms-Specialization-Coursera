#include <bits/stdc++.h>
using namespace std;
bool comparator(string a,string b)
{
    string ab,ba;
    ab=a.append(b);
    ba=b.append(a);

    if(ab.compare(ba)>0)
        return true;
    return false;
}
void display(vector<string>v,int n)
{
    sort(v.begin(),v.end(),comparator);
    for(int i=0;i<n;i++)
    {
        cout<<v[i];
    }
}
int main()
{
    int n;
    cin>>n;
    vector<string>v(n);
    for(int i=0;i<n;i++)
    {
        cin>>v[i];
    }
    display(v,n);
    return 0;
}
print("this was max prizes")
