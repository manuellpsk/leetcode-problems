from main import Solution


def test_1():
    assert Solution().convertToTitle(1) == 'A'


def test_2():
    assert Solution().convertToTitle(28) == 'AB'


def test_3():
    assert Solution().convertToTitle(701) == 'ZY'


def test_4():
    assert Solution().convertToTitle(702) == 'ZZ'
