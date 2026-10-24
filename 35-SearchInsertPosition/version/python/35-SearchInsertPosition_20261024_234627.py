# Last updated: 24/10/2026, 23:46:27
1class Solution:
2    def searchInsert(self, nums: list[int], target: int) -> int:
3        l=0
4        r=len(nums)-1
5        while(l<=r):
6            mid=(l+r)//2
7            if nums[mid] == target:
8                return mid
9            elif nums[mid] > target:
10                r = mid - 1
11            else:
12                l = mid + 1
13        return l
14