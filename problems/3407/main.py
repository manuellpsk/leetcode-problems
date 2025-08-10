import re


class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # Slow way
        # return bool(re.search(p.replace('*', '.*'), s))
        sp = p.split("*")
        i = 0
        while sp:
            np = sp.pop(0)
            start = s.find(np, i)
            if start == -1:
                return False
            if len(sp) == 0:
                return True
            i = start + len(np)
