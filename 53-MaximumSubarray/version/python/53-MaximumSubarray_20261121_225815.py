# Last updated: 21/11/2026, 22:58:15
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:            
3        res = nums[0]
4        total = 0
5
6        for n in nums:
7            if total < 0:
8                total = 0
9
10            total += n
11            res = max(res, total)
12        
13        return res