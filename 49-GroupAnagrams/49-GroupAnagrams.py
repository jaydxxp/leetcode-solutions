# Last updated: 10/11/2026, 23:26:02
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result={}
        for i in strs:
            key="".join(sorted(i))
            if key not in result:
                result[key]=[]
            result[key].append(i)
        return list(result.values())
