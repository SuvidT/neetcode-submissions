class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        l_prod = 1
        for i in range(len(nums)):
            result[i] *= l_prod
            l_prod *= nums[i]

        r_prod = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= r_prod
            r_prod *= nums[i]

        return result