// Last updated: 25/07/2026, 12:27:27
class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false;
        int og=x;
        int digit;
        long rev=0;
        while(x>0)
        {
            digit=x%10;
            rev=rev*10+digit;
            x=x/10;
        }
        return og==rev;
    }
};