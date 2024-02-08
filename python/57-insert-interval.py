"""
Date: Feb 07, 2024
Last Revision: N/A
General Notes: 
- 97ms runtime (11.24%) and 19.76MB (96.14%)
- I think most people created a new array and returned it so thats why have lower runtime but more memory
- Question asked us to return original array though
Solution Notes:
- Add new interval to existing array and sort by start number
- Iterate through the intervals and merge them if they overlap
- Return the intervals
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # add new interval to existing array
        intervals.append(newInterval)

        # if only one interval (the one we just added), problem is solved
        if len(intervals) == 1: return intervals

        # sort the intervals by the start number
        intervals.sort(key = lambda x:x[0])

        # iterate through the intervals and merge them if they overlap
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
