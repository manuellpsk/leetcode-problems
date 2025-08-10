from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for _ in range(m, len(nums1)):
            nums1.pop(m)
        nums1.extend(nums2)
        nums1.sort()
        return nums1
