class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = set()
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

            if len(freq) < k:
                freq.add(num)
            else:
                replace = ('\0',)
                for f in freq:
                    if num not in freq and counter[f] < counter[num]:
                        replace = (f,)
                if replace != ('\0',):
                    freq.remove(replace[0])
                    freq.add(num)


        return list(freq)