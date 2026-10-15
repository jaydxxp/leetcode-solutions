# Last updated: 16/10/2026, 02:20:29
1class Solution:
2    def frequencySort(self, s: str) -> str:
3        freq={}
4        for i in s:
5            if i in freq:
6                freq[i]+=1
7            else:
8                freq[i]=1
9        chars=list(freq.keys())
10        for i in range(len(chars)):
11            for j in range(i+1,len(chars)):
12                if freq[chars[j]]>freq[chars[i]]:
13                    chars[i],chars[j]=chars[j],chars[i]
14                elif freq[chars[i]]==freq[chars[j]] and chars[i]>chars[j]:
15                    chars[i],chars[j]=chars[j],chars[i]
16        result=""
17        for i in chars:
18            result+=i*freq[i]
19        return result