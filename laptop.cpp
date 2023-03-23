#include<iostream>
using namespace std;

int main()
{
    int wc, hc, ws, hs;
    cin>>wc>>hc>>ws>>hs;
    if (wc-1 > ws && hc-1 > hs)
    {
        cout<<1<<endl;
    }
    else
    {
     cout<<0<<endl;
    }

    return 0;


}