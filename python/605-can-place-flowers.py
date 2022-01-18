"""
Date: Jan 17 2022
Last Revision: N/A
General Notes: 
- 176ms runtime (49.44%) and 14.6MB (61.08%)
Solution Notes:
- iterate through the flowerbed and see if there is an available spot to plant the flower
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        available_spots = 0
        i = 0
        while i < len(flowerbed):
            if (flowerbed[i] == 0) and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1]==0):
                flowerbed[i] = 1
                available_spots += 1
                if available_spots >= n: return True
            
            i += 1
                
        return available_spots >= n
