# Last updated: 19/11/2026, 23:22:10
class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        return min(map(sub, nlargest(3, nums), reversed(nsmallest(3, nums))))