# Last updated: 25/11/2026, 20:25:48
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3
4        left = 1
5        right = max(piles)
6
7        while left < right:
8
9            mid = (left + right) // 2
10
11            total_hours = 0
12
13            for pile in piles:
14                total_hours += (pile + mid - 1) // mid
15
16            if total_hours <= h:
17                right = mid
18
19            else:
20                left = mid + 1
21
22        return left