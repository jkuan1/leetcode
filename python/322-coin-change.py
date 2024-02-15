"""
Date: Feb 15 2024
Last Revision: N/A
General Notes: 
- 733ms runtime (84.25%) and 16.90MB (92.60%)
Solution Notes:
- Use a memoList to keep track of the minimum number of coins needed to make each amount
"""

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        # initialize memoList with len amount + 1 to make sure we can find the minimum values in range of 0 to amount
        # set initial value of coins need to reach i to amount + 1 (which cannot be reached because smallest coin is 1)
        memoList = [amount + 1] * (amount + 1)
        memoList[0] = 0 # memoization base case

        # iterate through the memoList to find the minimum number of coins needed to make each amount
        for i in range(0, len(memoList)):
            for coin in coins:
                if coin <= i:
                    # if curr amount can be reached with current coin, then memoList[i - coin] + 1 will be the least number of coins needed to reach i
                    # if curr amount can't be reached, min will be comparing amount + 1 to amount + 1 + 1
                    memoList[i] = min(memoList[i], memoList[i - coin] + 1)

        # if memoList[amount] is amount + 1, then amount cannot be reached with the given coins so return -1
        if memoList[amount] == amount + 1: 
            return -1 
        
        # else, return the minimum number of coins needed to reach amount
        else: 
          return memoList[amount]