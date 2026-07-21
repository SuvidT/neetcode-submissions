class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currArea = 0
        r = 0
        l = len(heights) -1


        for x in heights:
            area = min(heights[r], heights[l]) * (l-r)
            if area > currArea:
                currArea = area
            if heights[r] <= heights[l]:
                r += 1
            else:
                l -= 1
        
        return currArea