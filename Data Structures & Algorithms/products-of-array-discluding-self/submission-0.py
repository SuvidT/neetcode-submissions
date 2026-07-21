class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(final)):
                if i != j:
                    final[j] *= nums[i]
        return final