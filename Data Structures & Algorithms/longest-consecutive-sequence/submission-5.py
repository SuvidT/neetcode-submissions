class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        best = 0

        for n in num_set:
            # Check if 'n' is the start of a sequence
            if (n - 1) not in num_set:
                length = 1
                
                # Count consecutive numbers going forward
                while (n + length) in num_set:
                    length += 1
                
                best = max(best, length)

        return best