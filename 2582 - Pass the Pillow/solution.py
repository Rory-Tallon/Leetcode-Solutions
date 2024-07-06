class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        multiple = time // (n - 1)
        r = time % (n-1)
        
        if multiple % 2 == 0:
            return 1 + r
        else:
            return n - r
