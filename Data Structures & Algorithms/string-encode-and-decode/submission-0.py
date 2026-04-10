class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        sizes = [str(len(s)) for s in strs]
        res += ", ".join(sizes) + "#"
        for s in strs:
            res += s

        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        s = s.split("#", 1)
        sizes = s[0].split(", ")
        res = []
        ind = 0
        for size in sizes:
            res.append(s[1][ind: ind+int(size)])
            ind += int(size)
        return res