from main import Solution


def test_1():
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    output = True
    assert Solution().canPlaceFlowers(flowerbed, n) == output


def test_2():
    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    output = False
    assert Solution().canPlaceFlowers(flowerbed, n) == output


def test_3():
    flowerbed = [1, 0, 0, 0, 0, 1]
    n = 2
    output = False
    assert Solution().canPlaceFlowers(flowerbed, n) == output
