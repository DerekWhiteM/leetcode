class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 2
        for _ in range(n - 2):
            next = a + b
            a = b
            b = next
        return b
