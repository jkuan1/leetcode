"""
Date: Jan 10 2022
Last Revision: N/A
General Notes: 
- Super tired doing this today... Took advantage of some built-in functions and went with it. 
- 68ms runtime (5.46%) and 14.3MB (22.51%)
- Would like to revisit to make a solution that is faster 
Solution Notes:
- convert a and b into base 10 using int(x,2). Add them together and convert to binary using bin(). Turn to string and remove the standard 0b.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a,2) + int(b,2)))[2:]
            