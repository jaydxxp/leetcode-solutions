# Last updated: 10/11/2026, 03:36:37
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        longest=""
4        def expand(left,right):
5            while left>=0 and right<len(s) and s[left]==s[right]:
6                left-=1
7                right+=1
8            return s[left+1:right]
9        for i in range(len(s)):
10            odd=expand(i,i)
11            even=expand(i,i+1)
12            if len(odd)>len(longest):
13                longest=odd
14            if len(even)>len(longest):
15                longest=even
16        return longest
17