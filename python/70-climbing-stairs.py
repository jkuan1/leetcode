"""
Date: Feb 5 2024
Last Revision: N/A
General Notes: 
- 36ms runtime (54.46%) and 16.49MB (86.89%)
Solution Notes:
- Find the pattern in the problem - Will realize that F(n) = F(n-1) + F(n-2)
- n = 0 and n = 1 are base cases 
"""

class Solution:

    memo = {
        0: 1,
        1: 1
    }

    def climbStairs(self, n: int) -> int:

        if n not in self.memo:
            self.memo[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)

        return self.memo[n]