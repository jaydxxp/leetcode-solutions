// Last updated: 11/08/2026, 01:36:12
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n = nums.size();
        int i = 0;
        
        while (i < n) {
            int correct = nums[i] - 1;
            if(i==correct)
            {
                i++;
            }
            else if(nums[i]==nums[correct])
            {
                return nums[i];
            }
            else{
                swap(nums[i],nums[correct]);
            }
        }
        return 0;
        
    }
};