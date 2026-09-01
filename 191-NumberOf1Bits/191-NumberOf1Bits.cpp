// Last updated: 02/09/2026, 00:00:01
class Solution {
private:
    string ConvertBinary(int num)
    {
        string res="";
        while(num>0)
        {
            if(num%2==1)
            {
                res=res+"1";
            }
            else{
                res=res+'0';
            }
            num=num/2;
        }
        int l=0; int r=res.length()-1;
        while(l>r)
        {
            swap(res[l],res[r]);
            l++;
            r--;
        }
        return res;
    }
public:
    int hammingWeight(int n) {
        string binary=ConvertBinary(n);
        int calc=0;
        for(char c:binary)
        {
            if(c=='1')
            {
                calc=calc+1;
            }
        }
        return calc;
    }
};