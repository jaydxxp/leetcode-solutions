# Last updated: 21/10/2026, 00:00:17
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor==dividend:
            return 1
        if dividend==-(2**31) and divisor==-1:
            return 2**31-1
        if divisor==1:
            return dividend
        ans=0
        dv=abs(divisor)
        dd=abs(dividend)
        while(dv<=dd):
            total,count=dv,1
            while(total<dd-total):
                total+=total
                count+=count
            ans+=count
            dd-=total
        if divisor<0 and dividend>0: return -ans
        elif divisor>0 and dividend<0: return -ans
        return ans