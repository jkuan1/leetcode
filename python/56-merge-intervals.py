"""
Date: Feb 16, 2024
Last Revision: N/A
General Notes: 
- 124ms runtime (62.11%) and 20.60MB (87.16%)
Solution Notes:
- Iterate through the intervals and merge them if they overlap
- Return the intervals
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x:x[0])

        i = 1

        while i < len(intervals):

            currStart, currEnd, prevStart, prevEnd = intervals[i][0], intervals[i][1], intervals[i-1][0], intervals[i-1][1]
            
            # There is an overlap so we will make previous interval include the current one and then discard the current one
            if currStart <= prevEnd: 
                intervals[i-1][0] = min(currStart, prevStart)
                intervals[i-1][1] = max(currEnd, prevEnd)
                intervals.pop(i)
            else:
                i += 1
        
        return intervals