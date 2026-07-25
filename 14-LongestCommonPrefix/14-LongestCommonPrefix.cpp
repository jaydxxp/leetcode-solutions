// Last updated: 25/07/2026, 12:27:25
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(),strs.end());
        string first=strs[0];
        string last=strs[strs.size()-1];
        int n=strs.size();
        string ans="";
        for(int i=0;i<min(first.size(),last.size());i++)
        {
            if(first[i]!=last[i])
            {
                return ans;
            }
            ans=ans+first[i];
        }
        return ans;
    }
};