# Last updated: 19/11/2026, 23:21:51
1class Solution:
2    def minimizeSum(self, nums: list[int]) -> int:
3        return min(map(sub, nlargest(3, nums), reversed(nsmallest(3, nums))))