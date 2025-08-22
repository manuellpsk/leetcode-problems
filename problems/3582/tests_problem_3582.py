from main import Solution


def test_1():
    caption = "Leetcode daily streak achieved"
    output = "#leetcodeDailyStreakAchieved"
    assert Solution().generateTag(caption=caption) == output


def test_2():
    caption = "can I Go There"
    output = "#canIGoThere"
    assert Solution().generateTag(caption=caption) == output


def test_3():
    caption = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    output = "#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    assert Solution().generateTag(caption=caption) == output


def test_4():
    caption = "   "
    output = "#"
    assert Solution().generateTag(caption=caption) == output
