class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        remaining = {i: 0 for i in range(len(nums)+1)}

        for num in nums:
            remaining[num] = 1

        for num in remaining:
            if remaining[num] == 0:
                return num

        return -1