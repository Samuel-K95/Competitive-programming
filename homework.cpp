#include<iostream>
#include<cstring>

using namespace std;

int main()
{
    string num;
    getline(cin, num);
    int x=num.size();
    int count;
    for(int i=0; i<x; i++)
    {
        if (num[i]=='-')
        {
            string a, b;
            b=num[i+1];
            if(i==1)
            {
                a=num[i-1];
            }
            else
            {
                a=num[i-2];
                if(num[i-1]!='-'|| num[i-1]!=';'||num[i-1]!=' ')
                {
                    a+=num[i-1];
                }
            }
            if(num[i+2]!=' '|| num[i+2]!=';')
            {
                b+=num[i+2];
            }
            int c,d;
            c=stoi(a);
            d=stoi(b);
            for(int j=c; j < d; j++)
            {
                count++;
            }
        }
        if(num[i] ==';')
        {
            if( num[i-1]!='-' && num[i+2] !='-')
            {
                count++;
            }
        }
    }
    cout<<count<<endl;
    return 0;
}