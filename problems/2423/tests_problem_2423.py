from main import Solution


def test_1():
    word = "abcc"
    assert Solution().equalFrequency(word=word) is True


def test_2():
    word = "aazz"
    assert Solution().equalFrequency(word=word) is False


def test_3():
    word = "aa"
    assert Solution().equalFrequency(word=word) is True


def test_4():
    word = "aaabbbccc"
    assert Solution().equalFrequency(word=word) is False


def test_5():
    word = "abbccdd"
    assert Solution().equalFrequency(word=word) is True


def test_6():
    word = "aaabbccdd"
    assert Solution().equalFrequency(word=word) is True


def test_7():
    word = "abc"
    assert Solution().equalFrequency(word=word) is True
