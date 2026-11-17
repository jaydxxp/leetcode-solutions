# Last updated: 17/11/2026, 23:03:59
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        count=0
        longest=1
        temp=set()
        for i in nums:
            temp.add(i)
        for i in temp:
            if i-1 not in temp:
                count=1
                x=i
                while x+1 in temp:
                    x=x+1
                    count+=1
                longest=max(longest,count)
        return longest
