# Last updated: 27/11/2026, 23:14:07
1class Solution:
2    def productExceptSelf(self, nums: list[int]) -> list[int]:
3        result=[1]*len(nums)
4        left=1
5        for i in range(len(nums)):
6            result[i]=left
7            left*=nums[i]
8        right=1
9        for i in range(len(nums)-1,-1,-1):
10            result[i]*=right
11            right*=nums[i]
12        return result
13
14        