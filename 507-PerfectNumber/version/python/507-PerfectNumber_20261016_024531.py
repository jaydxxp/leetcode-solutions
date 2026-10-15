# Last updated: 16/10/2026, 02:45:31
1class Solution:
2    def checkPerfectNumber(self, num: int) -> bool:
3        if num == 1:
4            return False
5
6        ans = 1
7
8        for i in range(2, int(num**0.5) + 1):
9
10            if num % i == 0:
11                ans += i + num // i
12
13        return ans == num
14