"""
Date: Feb 21 2024
Last Revision: N/A
General Notes: 
- 31ms runtime (84.74%) and 16.60MB (79.43%)
- Did not enjoy this problem because it felt tedious to implement. Maybe there is a more fun solution that I did not think of
Solution Notes:
- Remember the direction of the spiral. 
- Depending on direction, we know what the next element to add to the answer is. Mark it as added by changing matrix cell to None value
- If we reach the end of the matrix, we will change direction
- If we encounter a None value, we know we have to backtrack one and then we will change direction
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        numRows, numCols = len(matrix), len(matrix[0])
        numElems = numRows * numCols
        ans = []
        i,j = 0,0

        direction = 'right'

        while len(ans) < numElems:
        
            value = matrix[i][j]
            
            if direction == 'right':
                if value is not None :
                    ans.append(value)
                    matrix[i][j] = None
                    if j + 1 < numCols:
                        j += 1
                    else:
                        i += 1
                        direction = 'down'

                else:
                    i += 1
                    j -= 1
                    direction = 'down'            
            
            elif direction == 'down':
                if value is not None:
                    ans.append(value)
                    matrix[i][j] = None
                    if i + 1 < numRows:
                        i += 1

                    else:
                        j -= 1
                        direction = 'left'

                else:
                    j -= 1
                    i -= 1
                    direction = 'left'
            
            elif direction == 'left':
                if value is not None:
                    ans.append(value)
                    matrix[i][j] = None
                    if j - 1 >= 0:
                        j -= 1
                    else:
                        i -= 1
                        direction = 'up'

                else:
                    i -= 1
                    j += 1
                    direction = 'up'
            
            elif direction == 'up':
                if value is not None:
                    ans.append(value)
                    matrix[i][j] = None
                    if i - 1 >= 0:
                        i -= 1
                    else:
                        j += 1
                        direction = 'right'
                else:
                    j += 1
                    i += 1
                    direction = 'right'
            
        return ans
                    



