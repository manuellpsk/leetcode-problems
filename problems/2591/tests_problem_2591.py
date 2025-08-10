from main import Solution


def test_1():
    money = 20
    children = 3
    expected = 1
    assert Solution().distMoney(money=money, children=children) == expected


def test_2():
    money = 16
    children = 2
    expected = 2
    assert Solution().distMoney(money=money, children=children) == expected


def test_3():
    money = 8
    children = 3
    expected = 0
    assert Solution().distMoney(money=money, children=children) == expected


def test_4():
    money = 15
    children = 2
    expected = 1
    assert Solution().distMoney(money=money, children=children) == expected


def test_5():
    money = 2
    children = 2
    expected = 0
    assert Solution().distMoney(money=money, children=children) == expected


def test_6():
    money = 1
    children = 2
    expected = -1
    assert Solution().distMoney(money=money, children=children) == expected


def test_7():
    money = 13
    children = 3
    expected = 1
    assert Solution().distMoney(money=money, children=children) == expected


def test_8():
    money = 17
    children = 2
    expected = 1
    assert Solution().distMoney(money=money, children=children) == expected
