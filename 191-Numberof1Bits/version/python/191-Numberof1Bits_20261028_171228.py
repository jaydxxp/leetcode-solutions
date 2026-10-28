# Last updated: 28/10/2026, 17:12:28
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        count=0
4        while(n>0):
5            count+=n&1
6            n>>=1
7        return count