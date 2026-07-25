// Last updated: 25/07/2026, 12:27:08
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int l=0;
        int r=arr.size()-1;
        
        
        while(l<=r)
        {
            int mid=(l+r)/2;
        
            if(arr[mid]<arr[mid+1])
            {
                l=mid+1;
              
            } 
            else
            {
                r=mid-1;
            }
        }
        return l;
    }
};