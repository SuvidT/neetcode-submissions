class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        s = strs[0]
        for x in strs[1:]:
            s += "<==x-x==>"
            s += x

        return s

    def decode(self, s: str) -> List[str]:
        return s.split("<==x-x==>")