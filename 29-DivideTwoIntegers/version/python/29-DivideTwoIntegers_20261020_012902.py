# Last updated: 20/10/2026, 01:29:02
1class Solution:
2    def divide(self, dividend: int, divisor: int) -> int:
3        if divisor==dividend:
4            return 1
5        if dividend==-(2**31) and divisor==-1:
6            return 2**31-1
7        if divisor==1:
8            return dividend
9        ans=0
10        dv=abs(divisor)
11        dd=abs(dividend)
12        while(dv<=dd):
13            total,count=dv,1
14            while(total<dd-total):
15                total+=total
16                count+=count
17            ans+=count
18            dd-=total
19        if divisor<0 and dividend>0: return -ans
20        elif divisor>0 and dividend<0: return -ans
21        return ans