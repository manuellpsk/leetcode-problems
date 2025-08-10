from main import Solution


def test_example_1():
    assert Solution().lengthOfLastWord("Hello World") == 5


def test_example_2():
    assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4


def test_example_3():
    assert Solution().lengthOfLastWord("luffy is still joyboy") == 6
