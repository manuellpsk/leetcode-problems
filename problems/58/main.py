class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        size = 0
        # reverse loop
        while i >= 0:
            char = s[i]
            if char == " ":
                if size > 0:
                    return size
            else:
                size += 1
            i -= 1
        return size
