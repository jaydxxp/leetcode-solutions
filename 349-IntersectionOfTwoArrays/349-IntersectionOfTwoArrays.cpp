// Last updated: 03/10/2026, 12:39:55
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        int n1=nums1.size();
        int n2=nums2.size();
        set<int> result;
        vector<int> l;
        int n=0;
        if(n1>n2)
        {
            n=n1;
        }
        else
        {
            n=n2;
        }
        for(int i=0;i<n;i++)
        {
            if(n==n1)
            {
                for(int j=0;j<n2;j++)
                {
                    if(nums1[i]==nums2[j])
                    {
                        result.insert(nums1[i]);
                        break;
                    }
                }
            }
            else
            {
                for(int j=0;j<n1;j++)
                {
                    if(nums2[i]==nums1[j])
                    {
                        result.insert(nums2[i]);
                        break;
                    }
                }
            }
        }
        for(int num:result)
        {
            l.push_back(num);
        }
        return l;
    }
};