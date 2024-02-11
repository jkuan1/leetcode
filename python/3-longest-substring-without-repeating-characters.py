"""
Date: Feb 10 2024
Last Revision: N/A
General Notes: 
- 50ms runtime (84.71%) and 16.60MB (88.13%)
- can make this more memory efficient by having a left and right pointer instead of a seperate substring variable
Solution Notes:
- Since we are looking for longest substring, we use a sliding window approach
- We will keep track of the longest substring encountered so far
- if we encounter a letter that is already in the substring, we will update the substring to accomodate the new letter
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        substring = ""

        for letter in s:
            if letter not in substring:
                substring = substring + letter
            else:
                ans = len(substring) if len(substring) > ans else ans
                substring = substring[substring.index(letter) + 1:] + letter

        ans = len(substring) if len(substring) > ans else ans
        return ans

