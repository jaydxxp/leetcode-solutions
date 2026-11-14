# Last updated: 14/11/2026, 23:14:41
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        result = set()
4        n = len(nums)
5
6        for i in range(n):
7            seen = set()
8            
9            for j in range(i + 1, n):
10                remain = -(nums[i] + nums[j])
11
12                if remain in seen:
13                    temp=[nums[i],nums[j],remain]
14                    temp.sort()
15                    result.add(tuple(temp))
16                seen.add(nums[j])
17
18        return [list(x) for x in result]