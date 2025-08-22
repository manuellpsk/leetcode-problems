from main import Solution


def test_1():
    nums = [3, 2, 5, 4]
    threshold = 5
    output = 3
    assert Solution().longestAlternatingSubarray(nums, threshold) == output


def test_2():
    nums = [1, 2]
    threshold = 2
    output = 1
    assert Solution().longestAlternatingSubarray(nums, threshold) == output


def test_3():
    nums = [2, 3, 4, 5]
    threshold = 4
    output = 3
    assert Solution().longestAlternatingSubarray(nums, threshold) == output


def test_4():
    nums = [4]
    threshold = 4
    output = 1
    assert Solution().longestAlternatingSubarray(nums, threshold) == output


def test_5():
    nums = [2, 2]
    threshold = 18
    output = 1
    assert Solution().longestAlternatingSubarray(nums, threshold) == output
