// Last updated: 02/09/2026, 00:40:10
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n<=0)
        {
            return false;
        }
        if (!(n & (n - 1))) {

            return true;
        }
        return false;
    }
};