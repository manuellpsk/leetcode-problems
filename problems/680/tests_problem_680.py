from main import Solution


def test_1():
    assert Solution().validPalindrome("aba") == True


def test_2():
    assert Solution().validPalindrome("abca") == True


def test_3():
    assert Solution().validPalindrome("abc") == False


def test_4():
    assert Solution().validPalindrome("a") == True

def test_4():
    assert Solution().validPalindrome("deeee") == True
