from main import Solution


def test_example_1():
    assert Solution().addBinary("11", "1") == "100"


def test_example_2():
    assert Solution().addBinary("1010", "1011") == "10101"
