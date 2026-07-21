class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict

        storedvals = defaultdict(int)

        for i, num in enumerate(nums):
            if (target - num) in storedvals:
                return [storedvals[target-num], i]

            storedvals[num] = i

        return []