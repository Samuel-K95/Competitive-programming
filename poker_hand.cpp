#include<iostream>
#include<cstring>


using namespace std;

int main()
{
    int sum;
    string arr;
    getline(cin, arr);
    int store[5], x= arr.size();
    string val[5];
    char rank[14]={'A','1','2','3','4','5','6','7','8','9','T','J','Q','K'};
    int c=0;
    for (int i =0; i< x; i++)
    {
        for(int j=0; j<x; j++)
        {
            if(arr[i] == rank[j])
            {
                val[c]= arr[i];
                c+=1;
            }
        }
    }
    
    for(int i=0; i<5; i++)
    {
        sum=0;
        for(int j=0; j< 5; j++)
        {
            if(val[i] == val[j])
            {
                sum+=1;
            }
        }
        store[i]=sum;
    }
    int max=store[0];
    for(int i=0; i<5; i++)
    {
        if (store[i]>max)
        {
            max=store[i];
        }
    }
    cout<<max;
    return 0;
}
