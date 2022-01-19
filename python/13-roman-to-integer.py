"""
Date: Jan 18 2022
Last Revision: N/A
General Notes: 
- 53ms runtime (48.88%) and 14.1MB (83.99%)
Solution Notes:
- iterate through the string and either catch the subtraction pair or just add the roman numeral
- I don't like how many if statements my code has.
- Future optimization is to simplify the code more
"""

class Solution:
    conversion = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    def romanToInt(self, s: str) -> int:
        
        sum, i = 0, 0
        
        while i < len(s):
            
            if s[i] not in ["I", "X", "C"] or i + 1 == len(s):
                sum += self.conversion[s[i]]            
            
            elif s[i] == "I" and s[i + 1] in ["V", "X"]:
                sum += self.conversion[s[i + 1]] - self.conversion[s[i]]
                i += 1
                print(i, "hi")
                
            elif s[i] == "X" and s[i + 1] in ["L", "C"]:
                sum += self.conversion[s[i + 1]] - self.conversion[s[i]]
                i += 1
            
            elif s[i] == "C" and s[i + 1] in ["D", "M"]:
                sum += self.conversion[s[i + 1]] - self.conversion[s[i]]
                i += 1
            
            else:
                sum += self.conversion[s[i]]
            
            i += 1
                
        return sum