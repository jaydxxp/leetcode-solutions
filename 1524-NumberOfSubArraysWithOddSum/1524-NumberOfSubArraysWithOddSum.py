# Last updated: 15/11/2026, 23:41:47
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        prefix=0
        even=1
        odd=0
        count=0
        mod=10**9+7
        for i in arr:
            count+=i
            if count%2==0:
                even+=1
            else:
                odd+=1
        return (even*odd)%mod
