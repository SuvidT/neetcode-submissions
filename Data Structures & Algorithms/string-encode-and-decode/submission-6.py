class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for x in strs:
            s += "<==x-x==>"
            s += x

        return s

    def decode(self, s: str) -> List[str]:
        return s.split("<==x-x==>")[1:]