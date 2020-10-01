#include <iostream>
using namespace std;
int main()
{
    for (int j=0;j<=5;j++)
    {
      for(int k=0;k<=5;k++)
     {
        cout<<k<<endl;
        if(k<3)
        {
            break;
        }
     }
   }
    return 0;
}
