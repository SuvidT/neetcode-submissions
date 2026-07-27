class Solution:
    def minOperations(self, logs: List[str]) -> int:

        dist_from_main = 0
        for log in logs:
            if log == '../':
                dist_from_main = 0

            elif log == './':
                pass

            else:
                dist_from_main += 2
        return dist_from_main