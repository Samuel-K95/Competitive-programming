#include <iostream>

using namespace std;

int main()
{
    int x, y, z, thick = 4;
    cin>>x>>y>>z;
    if (x-y > y)
    {
        y=x-y;
    }
    if(x-z > z)
    {
        z= x-z;
    }
    cout<< y*z*thick<<endl;

    return 0;
}