# Last updated: 15/11/2026, 23:41:28
1class Solution:
2    def numOfSubarrays(self, arr: list[int]) -> int:
3        prefix=0
4        even=1
5        odd=0
6        count=0
7        mod=10**9+7
8        for i in arr:
9            count+=i
10            if count%2==0:
11                even+=1
12            else:
13                odd+=1
14        return (even*odd)%mod
15