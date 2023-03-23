#include <iostream>
using namespace std;

int main()
{
    int x,y=0;
    cin>>x;
    int arr[x];
    for(int i=0; i<x; i++)
    {
        cin>>arr[i];
        if (arr[i]<0)
        {
            y-=arr[i];
        }
    }
    cout<<y<<endl;

}