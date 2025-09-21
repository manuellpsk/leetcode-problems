"""
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Constraints:

1 <= s.length, goal.length <= 2 * 104
s and goal consist of lowercase letters.
"""


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        i = 0
        letters_to_swap = ()
        while i < len(s):
            if s[i] != goal[i]:
                letters_to_swap = (*letters_to_swap, i)
            i += 1
        if not letters_to_swap:
            for c in s:
                if s.count(c) > 1:
                    return True
            return False
        if len(letters_to_swap) != 2:
            return False
        ia, ib = letters_to_swap
        aux = s[ia]
        s = s[:ia] + s[ib] + s[ia+1:]
        s = s[:ib] + aux + s[ib+1:]
        return s == goal
