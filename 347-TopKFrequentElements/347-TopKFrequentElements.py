# Last updated: 12/11/2026, 21:18:56
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        tu=sorted(freq.items(), key=lambda x: x[1])
        result=[]
        for i in range(len(tu)-1,len(tu)-k-1,-1):
            result.append(tu[i][0])
        return result
