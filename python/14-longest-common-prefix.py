"""
Date: Jan 25 2022
Last Revision: N/A
General Notes: 
- 50ms runtime (31.67%) and 14.2MB (81.87%)
Solution Notes:
- compare the first string with all the other strings in order of the letters and track the prefix
- return prefix if we find a word with a letter that does not match or we exceeded the length of a shorter word
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans = ""
        
        for i in range(0, len(strs[0])):
            letter = strs[0][i]
            
            for words in strs:
                
                if i == len(words) or words[i] != letter:
                    return ans 
                
            ans += letter
                
        return ans
