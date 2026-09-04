// Last updated: 05/09/2026, 02:52:12
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
  int n=nums.size()-1;
  unordered_map<int,bool> b;
    for(int i=0;i<=n;i++)
    {
        if(b[nums[i]]==true)
        {
            return true;
        }
        b[nums[i]]=true;
    }
    return false;
    }
};