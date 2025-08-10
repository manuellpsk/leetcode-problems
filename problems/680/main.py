class Solution:
    def validPalindrome(self, s: str) -> bool:
        ns = self.cadena_rara(s)
        if ns:
            if self.cadena_rara(ns[1:]) is None:
                return True
            if self.cadena_rara(ns[:-1]):
                return False
        return True

    def cadena_rara(self, s):
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return s[i:j+1]
