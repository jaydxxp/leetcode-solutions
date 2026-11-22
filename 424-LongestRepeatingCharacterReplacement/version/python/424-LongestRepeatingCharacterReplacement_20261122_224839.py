# Last updated: 22/11/2026, 22:48:39
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        count = {}
4        left = 0
5        ans = 0
6        max_freq = 0
7
8        for right in range(len(s)):
9            ch = s[right]
10            count[ch] = count.get(ch, 0) + 1
11
12            max_freq = max(max_freq, count[ch])
13
14            if (right - left + 1) - max_freq > k:
15                count[s[left]] -= 1
16                left += 1
17
18            ans = max(ans, right - left + 1)
19
20        return ans