# Last updated: 25/10/2026, 23:44:45
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s)!=len(t):
4            return False
5        return sorted(s)==sorted(t)