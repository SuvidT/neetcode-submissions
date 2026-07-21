class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = []
        frequency = defaultdict(int)
        result = []

        for a in range(len(nums)):
            count.append([])

        for i in nums: 
            frequency[i] += 1
        
        for j in frequency:
            count[frequency[j] -1].append(j)

        for x in range(len(nums)-1, -1, -1):
            for l in count[x]:
                if len(result) < k:
                    result.append(l)

        return result