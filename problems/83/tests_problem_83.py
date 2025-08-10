# from main import Solution, ListNode


# def test_1():
#     l_result = ListNode(1, ListNode(2))
#     l_output = Solution().deleteDuplicates(ListNode(1, ListNode(1, ListNode(2))))
#     while l_output.next and l_result.next:
#         assert l_output.val == l_result.val
#         l_output = l_output.next
#         l_result = l_result.next


# def test_2():
#     l_result = ListNode(1, ListNode(2, ListNode(3)))
#     l_output = Solution().deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))))
#     while l_output.next and l_result.next:
#         assert l_output.val == l_result.val
#         l_output = l_output.next
#         l_result = l_result.next
