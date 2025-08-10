from main import Solution


def test_1():
    nums = [1, 2, 10, 5, 7]
    output = True
    assert Solution().canBeIncreasing(nums) == output


def test_2():
    nums = [2, 3, 1, 2]
    output = False
    assert Solution().canBeIncreasing(nums) == output


def test_3():
    nums = [1, 1, 1]
    output = False
    assert Solution().canBeIncreasing(nums) == output


def test_4():
    nums = [100, 21, 100]
    output = True
    assert Solution().canBeIncreasing(nums) == output


def test_5():
    nums = [105, 924, 32, 968]
    output = True
    assert Solution().canBeIncreasing(nums) == output


def test_6():
    nums = [100, 21, 3]
    output = False
    assert Solution().canBeIncreasing(nums) == output
