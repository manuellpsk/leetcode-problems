from main import Solution


def test_1():
    assert Solution().isPowerOfTwo(1)


def test_2():
    assert Solution().isPowerOfTwo(2)


def test_3():
    assert Solution().isPowerOfTwo(3) is False


def test_4():
    assert Solution().isPowerOfTwo(0) is False


def test_5():
    assert Solution().isPowerOfTwo(-1) is False
