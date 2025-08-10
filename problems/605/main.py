from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        seeds = 0
        for i in range(0, len(flowerbed)):
            current = flowerbed[i]
            _next = 0 if i == len(flowerbed) - 1 else flowerbed[i+1]
            if current == 0 and prev == 0 and _next == 0:
                seeds += 1
                current = 1
            prev = current
        return n <= seeds
