from main import Solution


def test_example_1():
    assert Solution().strStr("sadbutsad", "sad") == 0


def test_example_2():
    assert Solution().strStr("leetcode", "leeto") == -1
