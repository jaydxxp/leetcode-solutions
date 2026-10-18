# Last updated: 19/10/2026, 02:48:30
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1={}
        freq2={}
        for i in s:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        for i in t:
            if i in freq2:
                freq2[i]+=1
            else:
                freq2[i]=1
        return freq1==freq2