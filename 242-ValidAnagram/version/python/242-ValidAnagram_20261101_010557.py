# Last updated: 01/11/2026, 01:05:57
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        s=sorted(s)
4        t=sorted(t)
5        return s==t