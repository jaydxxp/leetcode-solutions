// Last updated: 05/09/2026, 01:35:22
class Solution {
private:
    int Max(vector<int>& arr,int j)
    {
        int max=INT_MIN;
        for(int i=0;i<=j;i++)
        {
            if(arr[i]>max)
            {
                max=arr[i];
            }
        }
        return max;
    }
    int Min(vector<int>& arr,int j)
    {
        int min=INT_MAX;
        for(int i=j;i<arr.size();i++)
        {
            if(arr[i]<min)
            {
                min=arr[i];
            }
        }
        return min;
    }
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int smallscore=0;
        for(int i=0;i<nums.size();i++)
        {
            int max=Max(nums,i);
            int min=Min(nums,i);
            int score=max-min;
            if(score<=k)
            {
                return i;
            }
            
        }
        return -1;
    }
};