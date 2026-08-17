// Last updated: 18/08/2026, 02:14:01
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int i = 0;
        int n = nums.size();
        while (i < n) {
            if(nums[i] >= 1 && nums[i] <= n){
                int correct = nums[i] - 1;
            if ( nums[i] != nums[correct]) {
                swap(nums[i], nums[correct]);
            }
            else{
                i++;
            }
            }
             else {
                i++;
            }
        }
        for (int i = 0; i < n; i++) {
            if (nums[i] != i+1) {
                return i + 1;
            }
        }
        return n + 1;
    }
};