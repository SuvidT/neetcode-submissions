class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter

        counts = Counter(arr)

        for count in counts:
            if counts[count] == 1:
                k -= 1

            if k == 0:
                return count

        return ""