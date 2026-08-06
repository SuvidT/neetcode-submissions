class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                L = nums[l]
                R = nums[r]


                threesum = num + L + R

                if threesum > 0:
                    r -= 1

                elif threesum < 0:
                    l += 1

                else:
                    res.append([num, L, R])
                    l += 1
                    while l < r and L == nums[l]:
                        l += 1

        return res