from itertools import groupby


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        a = []
        for c in name:
            if a and a[-1][0] == c:
                a[-1][1] += 1
            else:
                a.append([c, 1])
        b = []
        for t in typed:
            if b and b[-1][0] == t:
                b[-1][1] += 1
            else:
                b.append([t, 1])

        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i][0] != b[i][0]:
                return False
            elif a[i][1] > b[i][1]:
                return False
        return True
