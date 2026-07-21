class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        maxR = height[-1]

        l = 0
        r = len(height) - 1

        vol = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                vol += max(0, min(maxL, maxR) - height[l])
                maxL = max(maxL, height[l])
            else:
                r -= 1
                vol += max(0, min(maxL, maxR) - height[r])
                maxR = max(maxR, height[r])
        
        return vol

            