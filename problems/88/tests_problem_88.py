from main import Solution


def test_1():
    assert Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3) == [1, 2, 2, 3, 5, 6]


def test_2():
    assert Solution().merge(nums1=[1], m=1, nums2=[], n=0) == [1]


def test_3():
    assert Solution().merge(nums1=[0], m=0, nums2=[1], n=1) == [1]
