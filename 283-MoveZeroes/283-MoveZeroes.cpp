// Last updated: 02/10/2026, 16:03:39
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int left = 0;
        int right = 0;
        while (right < nums.size()) {
            if (nums[right] != 0) {
                swap(nums[right], nums[left]);
                left++;
            }
            right++;
        }
    }
};