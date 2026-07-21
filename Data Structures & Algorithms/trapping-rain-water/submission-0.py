class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []
        minLR = 0

        for i in range(len(height)):
            j = len(height) - 1 -i

            if i == 0:
                maxLeft.append(height[i])
                maxRight.insert(0, height[j])
            else:
                maxLeft.append(max(height[i], maxLeft[-1]))
                maxRight.insert(0, max(height[j], maxRight[0]))
        
        for a in range(len(height)):
            minLR += max(0, min(maxLeft[a], maxRight[a]) - height[a])
        
        return minLR