"""
Date: Feb 2 2024
Last Revision: N/A
General Notes: 
- 754ms runtime (74.18%) and 27.34MB (83.72%)
- O(n) runtime which I don't think I can get much better
Solution Notes:
- Left pointer represents best current buy point
- Right pointer represents current sell point (gets iterated)
- In any given iteration of the array I start with:
    - The best potential buy point
    - The current max profit
- If the left pointer is less than the right pointer, I check if using the current day as the sell point would lead to higher profit than what is recorded
- If the left pointer is less than the right pointer, I update left pointer to be the next best potential buy point
- This means that in the next iteration, my resources from the current iteration moves forward
- By the last iteration, I will have the current max profit which is the answer
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left_pointer = 0 #buy point
        right_pointer = 1 #sell point
        max_profit = 0

        while right_pointer < len(prices):
            curr_profit = prices[right_pointer] - prices[left_pointer]
            if prices[left_pointer] < prices[right_pointer]:
                max_profit = max(curr_profit, max_profit)
            else:
                left_pointer = right_pointer
            right_pointer += 1
        
        return max_profit