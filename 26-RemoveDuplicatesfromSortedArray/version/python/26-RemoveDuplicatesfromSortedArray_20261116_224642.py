# Last updated: 16/11/2026, 22:46:42
1class Solution:
2    def removeDuplicates(self, nums: list[int]) -> int:
3        i=0
4        for j in range(1,len(nums)):
5            if nums[i]!=nums[j]:
6                i+=1
7                nums[i]=nums[j]
8        return i+1