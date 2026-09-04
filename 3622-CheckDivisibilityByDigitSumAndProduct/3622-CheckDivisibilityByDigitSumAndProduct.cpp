// Last updated: 05/09/2026, 01:35:23
class Solution {
public:
    bool checkDivisibility(int n) {
        int og=n;
        int sum=0;
        int product=1;
        while(n>0)
        {
            int digit=n%10;
            sum=sum+digit;
            product = product * digit;
            n=n/10;
        }

        if(og%(sum+product)!=0)
        {
            return false;
        }
        return true;
    }
};