// Last updated: 05/09/2026, 01:35:39
class Solution {
private:
    int binary(int l,int r,vector<int>& nums, int target)
    {
        if(l>r)
        {
            return -1;
        }
    
            int mid = l + (r - l) / 2;
            if(nums[mid]>target)
            {
                return binary(l,mid-1,nums,target);
            }
            else if(nums[mid]<target)
            {
                return binary(mid+1,r,nums,target);
            }
            else{
                return mid;
            }
     
      
    }

public:
    int search(vector<int>& nums, int target) {
     
        return binary(0,nums.size()-1,nums,target);
    }
};