import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        """
            It only contains lowercase letters, hyphens, and/or punctuation (no digits).

            There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters 
            ("a-b" is valid, but "-ab" and "ab-" are not valid).

            There is at most one punctuation mark. If present, it must be at the end of the token 
            ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
        """
        tokens = sentence.split()
        valid_words = 0
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        punctuation = ['!', '.', ',']
        for token in tokens:
            hyphen_c = 0
            is_hyphen_c = True
            # No digits
            for i, t in enumerate(token):
                if t in digits:
                    is_hyphen_c = False
                    break
                if t == "-":
                    if i == 0 or i == len(token) - 1:
                        is_hyphen_c = False
                        break
                    else:
                        if not (token[i-1].isalpha() and token[i+1].isalpha()):
                            is_hyphen_c = False
                            break
                    hyphen_c += 1
                if hyphen_c > 1:
                    is_hyphen_c = False
                    break
                if t in punctuation:
                    if i != len(token) - 1:
                        is_hyphen_c = False
                        break
            if is_hyphen_c:
                valid_words += 1
        return valid_words
