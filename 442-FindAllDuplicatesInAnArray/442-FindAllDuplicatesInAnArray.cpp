// Last updated: 18/08/2026, 02:13:47
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int i=0;
        int n=nums.size();
        vector<int> soln;
        while(i<n)
        {
            int correct=nums[i]-1;
            if(nums[i]!=nums[correct])
            {
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
                soln.push_back(nums[i]);
            }
        }
        return soln;
    }
};