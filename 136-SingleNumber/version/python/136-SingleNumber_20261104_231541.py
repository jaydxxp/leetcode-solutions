# Last updated: 04/11/2026, 23:15:41
1class Solution:
2    def singleNumber(self, nums: list[int]) -> int:
3        xor=0
4        for i in nums:
5            xor^=i
6        return xor