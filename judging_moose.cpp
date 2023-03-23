#include<iostream>
#include<cstring>

using namespace std;

int main()
{
    int x, y, z;
    string word;
    cin>> x>>y;
    if (x==0 and y==0)
    {
        cout<<"Not a moose";
    }
    else
    {
        if (x!=y)
        {
            if (x>y)
            {
                z= x*2;
            }
            else if(y>x)
            {
                z=y*2;
            }
            word ="Odd";
        }
        else
        {
            z= x+y;
            word = "Even";
        }

        cout<<word<<" "<<z;
    }
    return 0;

}