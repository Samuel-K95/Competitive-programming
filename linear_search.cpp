#include <iostream>

using namespace std;

int main()
{
    int arr[]={4,5,6,7,8,9,10,12,13,15,16,17,18,24};
    int size=sizeof(arr)/sizeof(arr[0]);
    int first=arr[0];
    int last=arr[size-1];
    int target= 13;
    int mid, answer=0;
    while(first<=last)
    {
        mid = (first +last)/2;
        if(arr[mid]== target)
        {
            answer = mid;
            break;
        }
        else if(target > mid)
        {
            first = mid+1;
        }
        else if(target < mid)
        {
            last = mid-1;
        }
    }
    cout<<answer;
    
}