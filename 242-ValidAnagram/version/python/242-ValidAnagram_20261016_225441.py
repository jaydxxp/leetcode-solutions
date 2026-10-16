# Last updated: 16/10/2026, 22:54:41
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        s=sorted(s)
4        t=sorted(t)
5        if(s==t):
6            return True
7        return False