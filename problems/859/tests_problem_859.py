from main import Solution


def test_1():
    s = "ab"
    goal = "ba"
    output = True
    assert Solution().buddyStrings(s=s, goal=goal) == output


def test_2():
    s = "ab"
    goal = "ab"
    output = False
    assert Solution().buddyStrings(s=s, goal=goal) == output


def test_3():
    s = "abab"
    goal = "abab"
    output = True
    assert Solution().buddyStrings(s=s, goal=goal) == output
