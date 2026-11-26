# Last updated: 26/11/2026, 23:10:54
class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice=10
        i=0
        while n>=alice:
            n=n-alice
            alice=alice-1
            i+=1
        return i%2==1
