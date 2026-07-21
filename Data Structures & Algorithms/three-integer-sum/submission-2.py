class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #implementing merge sort
        def mergeSort(nums, L, R):
            if L < R:
                M = (L + R) // 2

                mergeSort(nums, L, M)
                mergeSort(nums, M+1, R)
                merge(nums, L, M, R)

        def merge(nums, L, M, R):
            left = [0] * (M - L + 1)
            right = [0] * (R - M)

            for i in range(0, len(left)):
                left[i] = nums[i + L]
            for j in range(0, len(right)):
                right[j] = nums[j + M + 1]

            i = 0
            j = 0
            k = L
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    k += 1
                    i += 1
                else:
                    nums[k] = right[j]
                    k += 1
                    j += 1
            
            while i < len(left):
                nums[k] = left[i]
                k += 1
                i += 1
            
            while j < len(right):
                nums[k] = right[j]
                k += 1
                j += 1
        
        mergeSort(nums, 0, len(nums) -1)

        result = []
        for a in range(len(nums)):
            if a > 0:
                if nums[a-1] == nums[a]:
                    continue
            l = a+1
            r = len(nums)-1
            while l < r:
                threeSum = nums[a] + nums[l] + nums[r]
                if threeSum == 0:
                    result.append([nums[a], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
            
        return result
