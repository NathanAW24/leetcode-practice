from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(f"node_val {self.val} node_next {self.next.val}")


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # slow fast, to find middle
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # reverse list for second half
        # slow.next because, slow is still at the last element of first list
        second_list = slow.next
        slow.next = None
        prev = None
        while second_list != None:
            tmp = second_list.next
            second_list.next = prev
            prev = second_list
            second_list = tmp

        # merge first and second list
        first_list = head
        second_list = prev
        while second_list != None or first_list != None:
            # store original next values
            original_first_list_next = first_list.next
            original_second_list_next = second_list.next

            # reorder the values first
            first_list.next = second_list
            second_list.next = original_first_list_next

            # set the first and second list pointer to the values they previously should hold before re-ordering
            first_list = original_first_list_next
            second_list = original_second_list_next

        return

    def checker(self, head):
        node = head
        self.reorderList(node)

        while node != None:
            print(node)
            node = node.next


nodeFive = ListNode(5)
nodeFour = ListNode(4, nodeFive)
nodeThree = ListNode(3, nodeFour)
nodeTwo = ListNode(2, nodeThree)
nodeOne = ListNode(1, nodeTwo)
Solution().checker(nodeOne)
