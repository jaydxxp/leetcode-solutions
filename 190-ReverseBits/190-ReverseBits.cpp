// Last updated: 03/09/2026, 00:19:54
class Solution {
public:
    int reverseBits(int n) {
        int mask=1;
        int reverse=0;
        for(int i=0;i<32;i++)
        {
            int bit=0;
            if(n&mask)
            {
                bit=1;
                reverse=reverse<<1;
                reverse=reverse+bit;
            }
            
            else{
                bit=0;
                reverse=reverse<<1;
                reverse=reverse+bit;
            }
            mask=mask<<1;
        }
        return reverse;
    }
};