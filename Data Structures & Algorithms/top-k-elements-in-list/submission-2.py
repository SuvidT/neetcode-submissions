class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hashMap = defaultdict(int)

        for i in nums:
            hashMap[i] += 1
            if len(result) < k:
                result.append(i)
            else:
                for j in range(0, len(result)):
                    if hashMap[i] > hashMap[result[j]] or i == result[j]:
                        continue
                    else:
                        result.insert(j, i)
                        result.pop(0)
        return result