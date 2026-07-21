class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        count = Counter(nums)

        buckets = [[] for x in range(len(nums) + 1)]

        for n, v in count.items():
            buckets[v].append(n)

        final = []
        for x in range(len(buckets)-1, 0, -1):
            for num in buckets[x]:
                if len(final) == k:
                    return final
                final.append(num)
                if len(final) == k:
                    return final

        return final
            