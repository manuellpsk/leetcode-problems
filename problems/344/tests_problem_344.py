from main import Solution


def test_1():
    s = ["h", "e", "l", "l", "o"]
    assert Solution().reverseString(s) == ["o", "l", "l", "e", "h"]


def test_2():
    s = ["H", "a", "n", "n", "a", "h"]
    assert Solution().reverseString(s) == ["h", "a", "n", "n", "a", "H"]


def test_3():
    s = ["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ",
         "a", " ", "c", "a", "n", "a", "l", ":", " ", "P", "a", "n", "a", "m", "a"]
    sol = ["a", "m", "a", "n", "a", "P", " ", ":", "l", "a", "n", "a", "c", " ", "a",
           " ", ",", "n", "a", "l", "p", " ", "a", " ", ",", "n", "a", "m", " ", "A"]
    new_s = Solution().reverseString(s)
    assert "".join(sol) == "".join(new_s)
