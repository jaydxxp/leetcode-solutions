// Last updated: 09/08/2026, 13:53:22
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int i=0;
        int n=nums.size();
        vector<int> missing;
        while(i<n){
            int correct=nums[i]-1;
            if( nums[i]!=nums[correct]){
                swap(nums[i],nums[correct]);
            }
            else{
                i++;
            }
        }
        for(int i=0;i<n;i++)
        {
            if(nums[i]!=i+1)
            {
                missing.push_back(i+1);
            }
        }
        return missing;
    }
};