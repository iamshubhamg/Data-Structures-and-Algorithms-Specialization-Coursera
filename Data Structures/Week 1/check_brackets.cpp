#include <iostream>
using namespace std;
int main()
{
    for (int j=0;j<=5;j++)
    {
      for(int i=0;i<=5;i++)
     {
        cout<<i<<endl;
        if(i<3)
        {
            break;
        }
     }
   }
    return 0;
}
