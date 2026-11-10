# Last updated: 10/11/2026, 23:24:57
1class Solution:
2    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
3        result={}
4        for i in strs:
5            key="".join(sorted(i))
6            if key not in result:
7                result[key]=[]
8            result[key].append(i)
9        return list(result.values())
10