# Last updated: 26/11/2026, 23:10:39
1class Solution:
2    def canAliceWin(self, n: int) -> bool:
3        alice=10
4        i=0
5        while n>=alice:
6            n=n-alice
7            alice=alice-1
8            i+=1
9        return i%2==1
10