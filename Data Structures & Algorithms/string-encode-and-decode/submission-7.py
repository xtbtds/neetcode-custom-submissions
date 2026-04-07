class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            d = ""
            while s[i] != "#" and s[i].isdigit():
                d += s[i]
                i+=1
            i+=1
            l = int(d)
            res.append(s[i:i+l])
            i+=l
        return res
        
