"""
Date: Feb 9 2024
Last Revision: N/A
General Notes: 
- 98ms runtime (86.79%) and 17.45MB (79.30%)
- Solution wants to take up only O(1) space
- Must edit original matrix in place
- matrix is m x n where 1<=m,n<=200
Solution Notes:
- I want to store the columns that need to be zeroed in the first row
- So I will first check if first row needs to be zeroed
- Go through rest of matrix normally and store columns that need to be zeroed in first row (with a zero)
- Go through first row again, zero all necessary columns
- Zero first row if necessary
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Get dimensions of matrix
        m, n = len(matrix), len(matrix[0])

        # Check if first row needs to be zeroed
        zero_first_row = False
        for j in range(0, n):
            if matrix[0][j] == 0: zero_first_row = True

        # Iterate through rest of rows
        for i in range(1, m):
            zero_the_row = False

            # If column needs to be zeroed, store in first row
            for j in range(0, n):
                if matrix[i][j] == 0: 
                    zero_the_row = True
                    matrix[0][j] = 0
            
            # Zero curr row if necessary
            if zero_the_row:
                matrix[i] = [0] * n

        # All columns that need to be zeroed are stored in first row so check in for loop
        for j in range(0, n):
            # If element in first row is zero, zero the column of the element
            if matrix[0][j] == 0:
                for i in range(1, m): matrix[i][j] = 0
        
        # Original check if first row contained zeros, if so we will zero it out now
        if zero_first_row: matrix[0] = [0] * n
        
        return