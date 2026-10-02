// Last updated: 02/10/2026, 16:03:31
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int first=0;
        int second=0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==1)
            {
                first++;
            }
            else{
                second=max(first,second);
                first=0;
            }
        }
        if(first>second){
            return first;
        }
        return second;
    }
};