class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0


        while l < r:
            area = (r - l) * min(heights[r], heights[l])

            if area > max_area:
                max_area = area

            if heights[r] < heights[l]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1

        return max_area