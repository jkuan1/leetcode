"""
Date: Feb 6 2024
Last Revision: N/A
General Notes: 
- 42ms runtime (59.00%) and 16.88MB (83.74%)
- BFS implementation so O(V+E) runtime
Solution Notes:
- Use a queue to implement BFS to traverse the graph
- Use a hashmap to store the cloned nodes
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node: return node
        
        # Implement BFS -> Have a queue (array) and a cloned_dict (hashmap)
        queue, clones_dict = [node], {node.val: Node(node.val, [])}

        while len(queue) > 0:

            curr_node = queue.pop()
            curr_clone = clones_dict[curr_node.val]
            
            for neighbor in curr_node.neighbors:
                if neighbor.val not in clones_dict: 
                    queue.append(neighbor)
                    clones_dict[neighbor.val] = Node(neighbor.val, [])
                curr_clone.neighbors.append(clones_dict[neighbor.val])

        return clones_dict[node.val]