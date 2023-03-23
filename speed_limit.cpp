#include <iostream>
#include<vector>
using namespace std;

int main()
{
    vector<int>answer;
    
    while(true)
    {
        int i;
        cin>>i;
        if (i == -1)
        {
            break;
        }
        else
        {
        int arr[i];
        int arr1[i];
        for(int j=0; j<i; j++)
        {
            cin>>arr[j]>>arr1[j];
        }
        int ans =0;
        for(int j=0; j<i; j++)
        {
            if (j=0)
            {
                ans +=arr[j]*arr1[j];
            }
            else
            {
                ans+= arr[j]* (arr1[j]- arr1[j-1]);
            }
            
        }
        answer.push_back(ans);
        }
    }
    int a=answer.size();
    for (int i =0; i< a; i++)
    {
        cout<<answer[i]<<" miles"<<endl;
    }
    return 0;
}
