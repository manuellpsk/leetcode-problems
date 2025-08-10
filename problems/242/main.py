class Solution:
    def is_anagram(self, s: str, t: str):
        data = {}
        while s != '':
            c = s[0]
            ocurrences = s.count(c)
            data[c] = ocurrences
            s = s.replace(c, '')
        for c, count in data.items():
            if t.count(c) != count:
                return False
            t = t.replace(c, '')
        return t == ''
