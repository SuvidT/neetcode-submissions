# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if pairs == []:
            return []
        import copy

        res = []
        res.append(copy.deepcopy(pairs))

        for i in range(1, len(pairs)):
            key = pairs[i]
            j = i - 1

            while j >= 0 and key.key < pairs[j].key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j+1] = key

            res.append(copy.deepcopy(pairs))

        return res