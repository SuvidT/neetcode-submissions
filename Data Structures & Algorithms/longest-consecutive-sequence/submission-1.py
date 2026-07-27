class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0;
        hashMap = {}
        lowest = nums[0]
        k = 1

        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
            if lowest > nums[i]:
                lowest = nums[i]
        
        hasNext = True
        nextNum = lowest
        while hasNext:
            if nextNum+1 in hashMap:
                k += 1
                nextNum += 1
            else:
                hasNext = False
        
        return k