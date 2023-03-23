#include<iostream>
#include<cstring>

using namespace std;

int main()
{
    int x;
    cin>>x;
    int store[x], answer[x], fact=1;
    for(int i = 0; i<x; i++)
    {
        cin>>store[i];
        fact=1;
        for(int j=1; j<=store[i]; j++)
        {
            fact*=j;
            
        }
        answer[i]=fact%10;
        
    }
    for(int i = 0; i<x; i++)
    {
        cout<<answer[i]<<endl;
    }
    return 0;

}


