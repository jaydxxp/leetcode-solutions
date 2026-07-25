// Last updated: 25/07/2026, 12:27:20
class Solution {
    private:
        int FirstPos(vector<int>&nums,int target)
        {
            int l=0;
            int r=nums.size()-1;
            int ans=-1;
            while(l<=r)
            {
                int mid=(l+r)/2;
                if(nums[mid]==target)
                {
                    ans=mid;
                    r=mid-1;
                }
                else if(nums[mid]<target)
                {
                    l=mid+1;
                }
                else
                {
                    r=mid-1;
                }
            }
            return ans;
        }
        int LastPos(vector<int>&nums,int target)
        {
            int l=0;
            int r=nums.size()-1;
            int ans=-1;
            while(l<=r)
            {
                int mid=(l+r)/2;
                if(nums[mid]==target)
                {
                    ans=mid;
                    l=mid+1;
                }
                else if(nums[mid]>target)
                {
                    r=mid-1;
                }
                else
                {
                    l=mid+1;
                }
            }
            return ans;
        }

public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int first=FirstPos(nums,target);
        int second= LastPos(nums,target);
        return {first,second};
    }
};