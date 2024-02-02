"""
Date: Jan 30 2024
Last Revision: N/A
General Notes: 
- 25ms runtime (98.39%) and 16.48MB (39.41%)
- Easy recursive solution, gonna try to do it iteratively next time
Solution Notes:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
        
        