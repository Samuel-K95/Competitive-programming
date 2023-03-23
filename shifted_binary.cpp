#include<iostream>
#include<vector>

using namespace std;

int main()
{
    int arr[]={1,2,3,-1,-2,-3,-4};
    int target = -2;
    int x=sizeof(arr)/sizeof(arr[0]);
    int first = arr[0];
    int last = x-1;
    int mid, answer;
    while(first<=last)
    {
        mid =first+(last-first)/2;
        if(arr[mid]== target)
        {
           answer=mid;
           break; 
        }
        else if(arr[first]<=arr[mid])
        {
            if(arr[first]<=target && target<arr[mid])
            {
                last=mid-1;
            }
            else
            {
                first=mid+1;
            }
        }
        else
        {
            if(arr[first]>=target && target>arr[mid])
            {
                first=mid+1;
            }
            else{
                last=mid-1;
            }
        }
        
    }
    cout<<answer;

}