# Last updated: 01/11/2026, 23:21:42
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while(n>0):
            count+=n&1
            n>>=1
        return count