# Last updated: 16/10/2026, 02:20:57
class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        chars=list(freq.keys())
        for i in range(len(chars)):
            for j in range(i+1,len(chars)):
                if freq[chars[j]]>freq[chars[i]]:
                    chars[i],chars[j]=chars[j],chars[i]
                elif freq[chars[i]]==freq[chars[j]] and chars[i]>chars[j]:
                    chars[i],chars[j]=chars[j],chars[i]
        result=""
        for i in chars:
            result+=i*freq[i]
        return result