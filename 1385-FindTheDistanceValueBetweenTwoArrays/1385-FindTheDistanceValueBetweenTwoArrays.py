# Last updated: 05/11/2026, 21:16:09
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count=0
        for i in arr1:
            flag=False
            for j in arr2:
                if abs(i-j)<=d:
                    flag=True
                    break
            if flag==False:
                count+=1
        return count