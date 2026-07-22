class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # { value : count }
        count = {}
        best = 0

        for i in range(len(nums)):
            num = nums[i]
            if (num-1) in count:
                count[num] = count[num-1] + 1
            else:
                count[num] = 1
            
            curr = num
            while (curr+1) in count:
                count[curr+1] = count[curr] + 1

                if best:
                    if count[curr+1] > best:
                        best = count[curr+1]
                else:
                    best = count[curr+1]
                curr += 1

            if best:
                if best < count[num]:
                    best = count[num]
            else:
                best = count[num]

        return best
            

