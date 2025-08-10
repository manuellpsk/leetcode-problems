class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        v = 1
        while v < n:
            v *= 2
        return v == n
