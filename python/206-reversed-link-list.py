"""
Date: Feb 8 2024
Last Revision: N/A
General Notes: 
- 30ms runtime (94.45%) and 18.20MB (54.43%)
Solution Notes:
- If linked list has zero or one element, return the linked list
- Else, create a new linked list and add the elements in reverse order
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # If linked list has zero or one element, return the linked list
        if head is None or head.next is None: return head

        # Create new Node with the first element of the linked list (no next node), it will be the last element of the new linked list
        newNode = ListNode(head.val, None)
        
        while head:
            # If there is a next element, add it to the new linked list
            if head.next is not None: 
                # new node is the value of the next element of original list and is linked to the previous newNode (to reverse the order of the orignal list)
                newNode = ListNode(head.next.val, newNode)
                head = head.next # iterate through while loop
            else:
                return newNode # if no next element in original list, return the new linked list with the most newly created node
        