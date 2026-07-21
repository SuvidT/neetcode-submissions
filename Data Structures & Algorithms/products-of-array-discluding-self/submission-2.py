class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # l pass
        l_pass = []
        l_prod = 1
        for l in nums:
            l_pass.append(l_prod)
            l_prod *= l

        print(l_pass)

        # r pass
        r_pass = []
        r_prod = 1
        for r in nums[-1::-1]:
            r_pass.insert(0, r_prod)
            r_prod *= r

        print(r_pass)

        # final pass
        final = []
        for i in range(len(nums)):
            final.append(l_pass[i] * r_pass[i])

        return final