#include<iostream>
#include<cstring>
#include<vector>
using namespace std;


int main()
{
    string word, val;
    getline(cin, word);
    vector<string>store;
    int x= word.size();
    for (int z=0; z<x; z++)
        {
            if (word[z]==' ')
            {
                break;
            }else
            {
                val+=word[z];
            }

        }
        store.push_back(val);
    for(int i=0; i<x; i++)
    {
        if (word[i] == ' ')
        {
            
            for (int j=i+1; j<x; j++)
            {
                
                if (word[j]==' ')
                {
                    val=" ";
                    for(int k=i+1; k<j; k++)
                    {
                        val+=word[k];
                    }
                    store.push_back(val);
                    break;
                    
                }
                
            }
            

        }
    }
    val=" ";
    for (int j =x; j>0; j--)
    {
        if (word[j]== ' ')
        {
            for (int a=j; a<x; a++)
            {
                val+=word[a];
            }
            store.push_back(val);
            break;
        }
    }
    vector<int>answer;
    int y= store.size();
    for(int i =0; i<=y; i++)
    {
        for( int j=0; j <=y; j++)
        {
            if (i==j)
            {
                continue;
            }
            else if( ("  "+store[i])== store[j])
            {
                answer.push_back(1);
            }
        }

    }
    for(int i=0; i< y; i++)
    {
        cout<<store[i]<<endl;
    }
    string final ="yes";
    int b= answer.size();
    for (int i =0; i< b; i++)
    {
        if (answer[i]==1)
        {
            final ="no";
            break;
        }
    }
    cout<<final<<endl;

    return 0;

}