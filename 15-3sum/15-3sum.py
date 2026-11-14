# Last updated: 14/11/2026, 23:15:49
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()
        n = len(nums)

        for i in range(n):
            seen = set()
            
            for j in range(i + 1, n):
                remain = -(nums[i] + nums[j])

                if remain in seen:
                    temp=[nums[i],nums[j],remain]
                    temp.sort()
                    result.add(tuple(temp))
                seen.add(nums[j])

        return [list(x) for x in result]