from main import Solution


def test_0():
    s = "hola"
    p = "ho*a"
    assert Solution().hasMatch(s, p) == True


def test_1():
    s = "eetcode"
    p = "ee*e"
    assert Solution().hasMatch(s, p) == True


def test_2():
    s = "car"
    p = "c*v"
    assert Solution().hasMatch(s, p) == False


def test_3():
    s = "luck"
    p = "u*"
    assert Solution().hasMatch(s, p) == True


def test_4():
    s = "jjj"
    p = "*j"
    assert Solution().hasMatch(s, p) == True


def test_5():
    s = "kvb"
    p = "k*v"
    assert Solution().hasMatch(s, p) == True
