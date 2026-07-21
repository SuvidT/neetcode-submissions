class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maping = {}

        for i in range(0, len(nums)):
            if target - nums[i] in maping:
                return [maping[target - nums[i]], i]
            else:
                maping[nums[i]] = i