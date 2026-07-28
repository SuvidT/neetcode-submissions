class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []

        l = 0
        r = 1
        while l < len(temperatures) - 1:
            greaterValExists = False
            while r < len(temperatures):
                if temperatures[l] < temperatures[r]:
                    output.append(r - l)
                    greaterValExists = True
                    break
                r += 1

            if not greaterValExists:
                output.append(0)

            l += 1
            r = l + 1

        output.append(0)

        return output
