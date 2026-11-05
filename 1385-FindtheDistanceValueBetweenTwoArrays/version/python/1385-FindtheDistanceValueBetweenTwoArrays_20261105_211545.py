# Last updated: 05/11/2026, 21:15:45
1class Solution:
2    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
3        count=0
4        for i in arr1:
5            flag=False
6            for j in arr2:
7                if abs(i-j)<=d:
8                    flag=True
9                    break
10            if flag==False:
11                count+=1
12        return count