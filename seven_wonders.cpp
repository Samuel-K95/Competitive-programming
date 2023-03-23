#include <iostream>
#include<cstring>
#include<vector>

using namespace std;

int main()
{
    string word, truth;
    int sum=0;
    getline(cin, word);
    char arr[3];
    vector<char>store;
    vector<int>store1;
    int x = word.size();
    for (int i=0; i<x; i++)
    {
        sum=0;
        for(int j=0; j<x; j++)
        {
            if(word[i]==word[j])
            {
                sum+=1;
            }
        }

        store1.push_back(sum*sum);
    }
    for(int i=0; i<x; i++)
    {
        cout<<store1[i];
    }
    /*int a = -1,b=-1,c=-1;
    for(int i=0; i<x; i++)
    {
        if(word[i]=='T')
        {
            if(i==a)
            {break;}
            else
            {
            for(int j=i; j<x; j++)
            {
                if(word[j]=='C')
                {
                    if(j==b)
                    {break;}
                    else
                    {
                    for(int k=j;k<x;k++)
                    {
                        if(word[k]=='G')
                        {
                            if(k==c)
                            {break;}
                            else
                            {
                            sum+=7;
                            a=i, b=j+1, c=k+1;
                            }
                        }
                    }
                    }
                }
            }
            }
        }
    }
    cout<<sum<<endl;*/

}