"""
Date: Feb 4 2024
Last Revision: N/A
General Notes: 
- 41ms runtime (31.24%) and 16.48MB (77.46%)
Solution Notes:
- Convert input to binary form and count the number of ones
- Not very efficient, want to revisit and use bitwise operators only one day
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_of_input = self.convertToBin(n)
        ans = 0
        for stringified_number in binary_of_input:
            if stringified_number == '1': ans += 1
        return ans 

    def convertToBin(self, n):
        ans = ""
        quotient = n % 2
        ans += str(quotient)
        if quotient == 1:
            n -= quotient
        n = n / 2

        while n > 0:
            quotient = n % 2
            ans += str(quotient)
            if quotient == 1:
                n -= quotient
            n = n / 2

        return ans