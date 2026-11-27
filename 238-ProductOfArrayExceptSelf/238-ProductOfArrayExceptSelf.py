# Last updated: 27/11/2026, 23:14:53
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result=[1]*len(nums)
        left=1
        for i in range(len(nums)):
            result[i]=left
            left*=nums[i]
        right=1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=right
            right*=nums[i]
        return result

        