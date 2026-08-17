// Last updated: 18/08/2026, 02:13:43
class Solution {
public:
    string reverseStr(string s, int k) {
        int i=0;
        int n= s.length();
        while(i<n)
        {
            int l=i;
            int r=min(i+k-1,n-1);
            while(l<r)
            {
                swap(s[l],s[r]);
                l++;
                r--;
            }
            i=i+(2*k);
        }
        return s;
    }
    
};