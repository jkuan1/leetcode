"""
Date: Jan 10 2022
Last Revision: N/A
General Notes: 
- 40ms runtime (58.82%) and 14.6MB (68.44%)
- Not a bad first attempt. I wonder if I could have optimized the code by not using str()
Solution Notes:
- Created a helper function that returns paths of tree recursively
- Add all paths together and return the sum
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        paths = self.getPathRecursive(root)
        
        ans = 0
        
        for i in paths:
            ans += int(i, 2)
        
        return ans
        
    def getPathRecursive(self, root):
        
        if root.left is None and root.right is None: return [str(root.val)]
        
        else:
            ans = []
            
            if root.left is not None: ans += self.getPathRecursive(root.left)
            if root.right is not None: ans += self.getPathRecursive(root.right)
                
            for i in range(0, len(ans)):
                ans[i] = str(root.val) + ans[i]
            
            return ans
                