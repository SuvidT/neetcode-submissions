class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0;
        
        hashMap = {}
        k = 1
        
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
        
        for i in nums:
            tempK = 1
            hasNext = True
            nextNum = i

            while hasNext:
                if nextNum + 1 in hashMap:
                    nextNum += 1
                    tempK += 1
                else:
                    hasNext = False

            if tempK > k:
                k = tempK
        
        return k