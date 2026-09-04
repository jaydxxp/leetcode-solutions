// Last updated: 05/09/2026, 01:35:36
class Solution {
private:
    int loop(int n)
    {
        if(n<2)
        {
            return n;
        }
        return loop(n-1)+loop(n-2);
    }
public:
    int fib(int n) {
       return loop(n);
    }
};