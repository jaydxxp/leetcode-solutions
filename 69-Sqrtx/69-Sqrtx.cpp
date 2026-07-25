// Last updated: 25/07/2026, 12:27:17
class Solution {
public:
    int mySqrt(int x) {
        if(x==0 || x==1)
        {
            return x;
        }
        int start=0;
        long end=x;
        while(start<=end)
        {
            int mid=start+(end-start)/2;
            if((long) mid*mid>(long)x)
            {
                end=mid-1;
            }
            else if(mid*mid==x)
            {
                return mid;
            }
            else
            {
                start=mid+1;
            }
        }
        return end;
    }
};