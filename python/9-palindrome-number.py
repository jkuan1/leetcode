"""
Date: Jan 13 2022
Last Revision: N/A
General Notes: 
- 48ms runtime (96.51%) and 14.3MB (16%)
Solution Notes:
- turn x into a string and see if the reverse of the string is equal to it
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        stringified = str(x)
        reverse = stringified[::-1]
        
        if reverse == stringified: 
            return True
        
        return False