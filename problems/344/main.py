from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            aux_i = s[i]
            aux_j = s[j]
            s[i] = aux_j
            s[j] = aux_i
            i += 1
            j -= 1
        return s
