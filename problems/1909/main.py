from typing import List


class Solution:
    def is_sorted(self, nums):
        i = 0
        while i < len(nums)-1:
            if nums[i] < nums[i+1]:
                i += 1
            else:
                return False
        return True

    def canBeIncreasing(self, nums: List[int]) -> bool:
        if self.is_sorted(nums):
            return True
        i = 0
        while i < len(nums):
            n_nums = nums[:i] + nums[i+1:]
            if self.is_sorted(n_nums):
                return True
            i += 1
        return False
