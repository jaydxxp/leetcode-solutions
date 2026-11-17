# Last updated: 17/11/2026, 23:03:05
1class Solution:
2    def longestConsecutive(self, nums: list[int]) -> int:
3        n=len(nums)
4        if n==0:
5            return 0
6        count=0
7        longest=1
8        temp=set()
9        for i in nums:
10            temp.add(i)
11        for i in temp:
12            if i-1 not in temp:
13                count=1
14                x=i
15                while x+1 in temp:
16                    x=x+1
17                    count+=1
18                longest=max(longest,count)
19        return longest
20