from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        fr_map = Counter(word)
        fr_values = list(fr_map.values())
        for i, f in enumerate(fr_values):
            x = fr_values.copy()
            if f-1 == 0:
                x.pop(i)
            else:
                x[i] = f-1
            if len(set(x)) == 1:
                return True
        return False
