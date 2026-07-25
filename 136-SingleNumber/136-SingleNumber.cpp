// Last updated: 25/07/2026, 12:27:14
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int index = 0;
        for (int i = 0; i < nums.size(); i++) {
            index = index ^ nums[i];
        }
        return index;
    }
};