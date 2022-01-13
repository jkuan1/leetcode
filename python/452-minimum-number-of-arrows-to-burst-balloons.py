"""
Date: Jan 13 2022
Last Revision: N/A
General Notes: 
- 2249ms runtime (10.57%) and 59MB (65.71%)
- Not a bad first attempt. I wonder if I could think of something that doesn't require sorting
- However, hard to think of a solution that is better than O(n) while mine is O(n*logn)... so is it worth considering the simplicity of the current solution?
Solution Notes:
- Greedy solution that "groups" balloons together based off their sorted end points
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda x:x[1])

        num_arrows, arrow = 0, None
        
        for point in points:
            if arrow is not None and point[0] <= arrow:
                pass #arrow pops current balloon
            else:
                arrow = point[1] #new arrow to pop current balloon
                num_arrows += 1
        return num_arrows