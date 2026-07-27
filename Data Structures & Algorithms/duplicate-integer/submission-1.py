class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newArray = []
        output = False

        for num in nums:
            for n in newArray:
                if n == num:
                    output = True
                    break
                newArray.append(num)
        
        return output