from main import Solution


def test_1():
    name = "alex"
    typed = "aaleex"
    output = True
    assert Solution().isLongPressedName(name, typed) == output


def test_2():
    name = "saeed"
    typed = "ssaaedd"
    output = False
    assert Solution().isLongPressedName(name, typed) == output


def test_3():
    name = ""
    typed = ""
    output = True
    assert Solution().isLongPressedName(name, typed) == output
