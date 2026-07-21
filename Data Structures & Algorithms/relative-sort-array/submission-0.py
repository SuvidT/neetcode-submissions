class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter

        count = Counter(arr1)
        finarr = []

        for num in arr2:
            for i in range(count[num]):
                finarr.append(num)
                arr1.remove(num)

        return finarr + sorted(arr1)