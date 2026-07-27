class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if nums[0] != 0:
            return 0

        last = 0
        for num in nums:
            if num != (last + 1):
                return last+1
            last = num