#include<bits/stdc++.h>
using namespace std;
void partition(long long a[],long long n,long long s,long long e,long long &x,long long &y)
{
   if (e - s <= 1)
   {
      if (a[e] < a[s])
         swap(a[e], a[s]);
      x = s;
      y = e;
      return;
   }
   long long mid = s;
   long long pivot = a[e];
   while (mid <= e) {
   if (a[mid]<pivot)
      swap(a[s++], a[mid++]);
      else if (a[mid]==pivot)
         mid++;
      else if (a[mid] > pivot)
         swap(a[mid], a[e--]);
   }
   x = s-1;
   y = mid;
}
void quicksort(long long a[],long long n,long long s,long long e)
{
    if(s>=e)
        return;
    long long x,y;
    partition(a,n,s,e,x,y);
    quicksort(a,n,s,x);
    quicksort(a,n,y,e);
}
int main()
{
    long long n;
    cin>>n;
    long long *a=new long long[n];
    for(long long i=0;i<n;i++)
        cin>>a[i];
    quicksort(a,n,0,n-1);
    for(long long i=0;i<n;i++)
        cout<<a[i]<<" ";
    return 0;
}
