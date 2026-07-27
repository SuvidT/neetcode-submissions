class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newArray = []
        output = false

        for num in nums:
            for n in newArray:
                if n == num:
                    output = true
                    break
                newArray.append(num)
        
        return output