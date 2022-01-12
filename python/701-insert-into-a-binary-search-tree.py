"""
Date: Jan 12 2022
Last Revision: N/A
General Notes: 
- 219ms runtime (11.84%) and 16.7MB (85.25%)
- Simple recursive solution. Thinking how I can make it faster without sacrificing simplicity.
Solution Notes:
- Base Case: If root is None, return TreeNode(val)
- Recursion: Recurse until you reach an appropriate leaf of the tree to insert the base case as a new leaf 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None:
            return TreeNode(val)
                
        elif val < root.val : 
            root.left = self.insertIntoBST(root.left, val)
        else: 
            root.right = self.insertIntoBST(root.right, val)

        return root