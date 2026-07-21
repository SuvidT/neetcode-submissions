class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dist_from_main = 0

        for log in logs:
            if log == '../':
                if dist_from_main > 0:
                    dist_from_main -= 1
            elif log == './':
                pass
            else:
                dist_from_main += 1

        return dist_from_main