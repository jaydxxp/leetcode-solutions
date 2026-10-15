# Last updated: 16/10/2026, 02:20:59
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        first=0
        second=0
        
        for i in nums:
            if i==1:
                first+=1
            elif i==0:
                second=max(first,second)
                first=0
        return max(first,second)
