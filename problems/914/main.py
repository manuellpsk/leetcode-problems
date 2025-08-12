from typing import List
from collections import Counter
import math


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        group_by = Counter(deck)
        values = list(set(group_by.values()))
        return math.gcd(*values) > 1
