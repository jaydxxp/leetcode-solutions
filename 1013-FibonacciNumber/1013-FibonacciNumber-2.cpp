//Recursive Solution
class Solution {
private:
    int loop(int n,int prev,int curr,int count)
    {
        if(n==count)
        {
            return curr;
        }
      
        int next=prev+curr;
        prev=curr;
        curr=next;
        return loop(n,prev,curr,count+1);
        
    }
public:
    int fib(int n) {
        if(n<2)
        {
            return n;
        }
        return loop(n,0,1,1);
    }
};
