"""
Date: Feb 2 2024
Last Revision: N/A
General Notes: 
- 33ms runtime (77.52%) and 16.67MB (58.142%)
- Want to revisit as the use of bitwise operators was hard because of lack of practice
Solution Notes:
- Since we cannot use "traditional" operators such as +-, used bitwise operators instead
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:

        
        # This solution works if integers are less than 32 bits (not the case in Python)
        # if b == 0: return a
        # return self.getSum(a ^ b, (a & b) << 1)

        # limit integers to 11 bits (problem description said a,b are in range [-1000,1000])
        mask = 0b11111111111 # 11 bits of 1's      
        MAX =  0b01111111111 # MAX following two's complement
        
        if b == 0:
            return a if a <= MAX else ~(a ^ mask)
        
        return self.getSum(
            (a ^ b) & mask,
            ((a & b) << 1) & mask
        )

