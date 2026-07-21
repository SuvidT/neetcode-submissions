class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter

        count = Counter(arr1)

        finarr = []
        for x in arr2:
            finarr.extend([x] * count[x])
            del count[x]

        leftovers = []
        for num, freq in count.items():
            leftovers.extend([num] * freq)


        return finarr + sorted(leftovers)