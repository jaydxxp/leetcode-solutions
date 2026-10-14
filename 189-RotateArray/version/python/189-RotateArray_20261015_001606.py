# Last updated: 15/10/2026, 00:16:06
1class Solution:
2    def rotate(self, nums: list[int], k: int) -> None:
3        n=len(nums)
4        k=k%n
5        rotated = [0] * n
6
7        for i in range(n):
8            rotated[(i + k) % n] = nums[i]
9        
10        for i in range(n):
11            nums[i] = rotated[i]