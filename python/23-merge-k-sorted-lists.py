"""
Date: Feb 13 2024
Last Revision: N/A
General Notes: 
- 86ms runtime (44.93%) and 19.85MB (69.05%)
- Would not be easy without built-in heapq
- Curious to try this in a language without a built-in heap (so I can implement my own)
Solution Notes:
- Given a list of ListNode objects in ascending value, we want to add the next node to heapq (priority queue) when the current node is linked to the answer
"""

import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = [] # initialize heap
        # add the first node of each list to the heap
        for i in range(len(lists)):
            if lists[i]:
                # Since we can't compare ListNode objects, we use the id of the object as a tiebreaker for heapq
                heapq.heappush(heap, (lists[i].val, id(lists[i]), i, lists[i]))
                lists[i] = lists[i].next

        # we want to retain the start of the list so we can return it if heap is not empty
        if heap: 
            _, _, i, start = heapq.heappop(heap)
            curr = start # we will return start at the end, curr will be used to help link the nodes together later
            # add the next node of the list that was just linked to the answer to the heap if it exists
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, id(lists[i]), i, lists[i]))
                lists[i] = lists[i].next

        # return if heap is empty
        else: return

        while heap:
            # link the highest priority node to curr to build our answer
            _, _, i, curr.next  = heapq.heappop(heap)
            curr = curr.next # move curr to the latest node for the next iteration
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, id(lists[i]), i, lists[i]))
                lists[i] = lists[i].next
        
        return start