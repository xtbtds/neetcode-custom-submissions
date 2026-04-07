class Solution:

    def encode(self, strs: List[str]) -> str:
        lens = []
        for s in strs:
            l = str(len(s))
            lens.append(l)
            lens.append(",")
        res = "".join(lens)
        res = res + "#"
        res = res + "".join(strs)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        lens, strs = s.split("#", 1)
        lens = list(lens.split(","))
        print(lens)
        for l in lens:
            if not len(l):
                break
            cur = int(l)
            if cur == 0:
                word = ""
                res.append(word)
                continue
            word = strs[start:start+cur]
            start += cur
            res.append(word)
        print(res)
        return res
        
