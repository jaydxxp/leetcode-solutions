# Last updated: 12/11/2026, 21:18:24
1class Solution:
2    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
3        freq={}
4        for i in nums:
5            if i not in freq:
6                freq[i]=1
7            else:
8                freq[i]+=1
9        tu=sorted(freq.items(), key=lambda x: x[1])
10        result=[]
11        for i in range(len(tu)-1,len(tu)-k-1,-1):
12            result.append(tu[i][0])
13        return result
14