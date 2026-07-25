// Last updated: 25/07/2026, 12:27:13
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l=0;
        int r=nums.size()-1;
        while(l<r)
        {
            int mid=l+(r-l)/2;
     
            if(nums[mid]<nums[mid+1])
            {
                l=mid+1;
            }
            else
            {
                r=mid;
            }
        }
        return l;
    }
};