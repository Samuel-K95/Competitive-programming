#include <iostream>

using namespace std;

int main()
{
    int x, sum, y;
    cin>>x;
    for (int i=x; ; i++)
    {
        y=i;
        sum=0;
        while (y>0)
        {
        sum+=y%10;
        y=y/10;
        }
        if (i%sum==0)
        {
            x=i;
            break;
        }
    }
    cout<<x;

}