from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            d = digits[i]
            nd = d + 1
            if nd > 9:
                digits[i] = nd % 10
                i -= 1
            else:
                digits[i] = nd
                return digits
        digits.insert(0, 1)
        return digits
