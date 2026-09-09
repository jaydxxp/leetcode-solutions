// Last updated: 10/09/2026, 00:05:07
class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int max = nums[0];
        vector<int> Min(nums.size());
        Min[nums.size()-1]=nums[nums.size()-1];
        for (int i = nums.size() - 2; i >= 0; i--) {
            Min[i] = min(nums[i],Min[i + 1]);
        }
        for (int i = 0; i < nums.size(); i++) {

            if (max < nums[i]) {
                max = nums[i];
            }

            if ((max - Min[i]) <= k) {
                return i;
            }
        }
        return -1;
    }
};