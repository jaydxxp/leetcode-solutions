# Last updated: 18/11/2026, 21:59:22
class Solution:
    def minChanges(self, s: str) -> int:
        return (int(s[::2], 2) ^ int(s[1::2], 2)).bit_count()