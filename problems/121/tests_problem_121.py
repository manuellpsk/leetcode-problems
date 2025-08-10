from main import Solution


def test_1():
    assert Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5


def test_2():
    assert Solution().maxProfit(prices=[7, 6, 4, 3, 1]) == 0


def test_3():
    assert Solution().maxProfit(prices=[2, 4, 1]) == 2


def test_4():
    assert Solution().maxProfit(prices=[2, 1, 2, 1, 0, 1, 2]) == 2
