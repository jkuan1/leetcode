
"""
Date: Feb 18 2024
Last Revision: N/A
General Notes: 
- 45ms runtime (65.59%) and 18.68MB (98.87%)
- Challenge is to try and get a solution with O(1) memory
Solution Notes:
- Since node values are integers, we can use the value to mark a node as visited
- If we encounter a visited node, we know there is a cycle
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        while head is not None:
            if head.val == 'visited': return True
            head.val = 'visited'
            head = head.next
        
        return False
