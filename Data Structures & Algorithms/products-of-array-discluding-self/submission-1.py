class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = [1] * len(nums)
        prefix = 1
        postfix = 1

        for i in range(0, len(nums)):
            final[i] = prefix
            prefix *= nums[i]
        
        for j in range (len(nums)-1, -1, -1):
            final[j] *= postfix
            postfix *= nums[j]
        
        return final