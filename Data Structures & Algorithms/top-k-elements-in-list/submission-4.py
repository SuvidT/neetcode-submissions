class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [0] * k
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

            replace = (-1, -1)
            for i, f in enumerate(freq):
                if counter[num] > f:
                    replace = (i, num)

            if replace[0] != -1:
                freq[replace[0]] = replace[1]

        return freq