from main import Solution


def test_example_1():
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2


def test_example_2():
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1


def test_example_3():
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
