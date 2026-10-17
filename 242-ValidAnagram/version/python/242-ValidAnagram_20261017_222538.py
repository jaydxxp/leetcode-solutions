# Last updated: 17/10/2026, 22:25:38
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        freq1={}
4        freq2={}
5        for i in s:
6            if i in freq1:
7                freq1[i]+=1
8            else:
9                freq1[i]=1
10        for i in t:
11            if i in freq2:
12                freq2[i]+=1
13            else:
14                freq2[i]=1
15        return freq1==freq2