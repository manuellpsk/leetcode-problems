from functools import reduce
import math
from typing import List


class Solution:
    """
        nums[l] % 2 == 0
    """

    def pass_even_odd_rule(self, nums: List[int], l: int, r: int):
        """
            For all indices i in thange [l, r - 1], nums[i] % 2 != nums[i + 1] % 2
        """
        values = [e % 2 for e in nums[l:r+1]]
        return all(a ^ b for a, b in zip(values, values[1:]))

    def pass_treshold_rule(self, sub_nums: List[int], threshold: int):
        """
            For all indices i in the range [l, r], nums[i] <= threshold
        """
        return all([n <= threshold for n in sub_nums])

    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_length = 0
        for l in range(len(nums)):
            num = nums[l]
            if num % 2 == 0:
                r = l
                while self.pass_treshold_rule(nums[l:r+1], threshold) and r < len(nums):
                    pass_even_odd_rule = self.pass_even_odd_rule(nums, l, r)
                    if pass_even_odd_rule:
                        length = r - l + 1
                        if length > max_length:
                            max_length = length
                    r += 1
        return max_length
