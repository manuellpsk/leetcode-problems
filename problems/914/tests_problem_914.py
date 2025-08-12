from main import Solution


def test_1():
    deck = [1, 2, 3, 4, 4, 3, 2, 1]
    output = True
    assert Solution().hasGroupsSizeX(deck) == output


def test_2():
    deck = [1, 1, 1, 2, 2, 2, 3, 3]
    output = False
    assert Solution().hasGroupsSizeX(deck) == output


def test_3():
    deck = [1, 1, 2, 2, 2, 2]
    output = True
    assert Solution().hasGroupsSizeX(deck) == output


def test_4():
    deck = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    output = True
    assert Solution().hasGroupsSizeX(deck) == output
