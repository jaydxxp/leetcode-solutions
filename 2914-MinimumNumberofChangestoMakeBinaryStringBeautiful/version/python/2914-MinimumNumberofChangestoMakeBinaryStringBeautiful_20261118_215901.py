# Last updated: 18/11/2026, 21:59:01
1class Solution:
2    def minChanges(self, s: str) -> int:
3        return (int(s[::2], 2) ^ int(s[1::2], 2)).bit_count()