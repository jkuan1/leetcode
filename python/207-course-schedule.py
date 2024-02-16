"""
Date: Feb 2 2024
Last Revision: N/A
General Notes: 
- 75ms runtime (99.49%) and 18.47MB (68.35%)
- Maybe can use deque instead of list to improve runtime even more
Solution Notes:
- Imagined problem as a directed graph and did topological sort 
- If there is a cycle, then the answer is False
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Store the descendants of each node in a list
        adjacencyList = [[] for _ in range(numCourses)]
        for n1, n2 in prerequisites:
            if n1 == n2: return False # Quick and easy cycle check to drastically reduce runtime
            adjacencyList[n2].append(n1)
        
        # Store the in-degrees of each node in a list
        inDegreesList = [0] * numCourses
        for n1, n2 in prerequisites:
            inDegreesList[n1] += 1

        # Create a queue of nodes with 0 in-degrees (course with no prerequisites)
        zeroInDegreesList = []
        for node in range(numCourses):
            if inDegreesList[node] == 0:
                zeroInDegreesList.append(node)

        count = 0

        while zeroInDegreesList:

            # Remove node with 0 in-degrees
            node = zeroInDegreesList.pop(0)
            count += 1

            for adjacentNode in adjacencyList[node]:
                # Check if removing the node with 0 in-degrees causes any other nodes to have 0 in-degrees
                inDegreesList[adjacentNode] -= 1
                if inDegreesList[adjacentNode] == 0:
                    zeroInDegreesList.append(adjacentNode)
        
        # If there is a cycle, then the count will be less than numCourses
        if count < numCourses: return False 
        return True