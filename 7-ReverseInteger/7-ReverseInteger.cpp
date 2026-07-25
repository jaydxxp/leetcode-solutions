// Last updated: 25/07/2026, 12:27:28
class Solution {
public:
    int reverse(int x) {
        int rev;
        int max=0;
        while(x!=0)
        {
            rev=x%10;
            if(max>INT_MAX/10 || max<INT_MIN/10) return 0;
            max=max*10+rev;
            x=x/10;
        }
        return max;
    }
};