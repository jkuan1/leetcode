"""
Date: Feb 13 2024
Last Revision: N/A
General Notes: 
- 44ms runtime (40.65%) and 17.54MB (93.32%)
Solution Notes:
- Simple recursive solution -> The depth of a tree is the maximum depth of its left and right subtrees + 1 
- Base case is when the root is None (depth of 0)
- But if the root has no children, the depth is 1, so we return 1 and save some time on an extra two recursive calls per branch
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root: return 0
        if not root.left and not root.right: return 1

        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)