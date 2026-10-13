# Last updated: 14/10/2026, 00:36:27
1class Solution:
2    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
3        first=0
4        second=0
5        
6        for i in nums:
7            if i==1:
8                first+=1
9            elif i==0:
10                second=max(first,second)
11                first=0
12        return max(first,second)
13