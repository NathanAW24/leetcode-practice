from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(f"node_val {self.val} node_next {self.next}")


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        n = 0
        nodeCounter = head
        while nodeCounter != None:
            n += 1
            nodeCounter = nodeCounter.next

        c = 0

        nodeL = head
        while n - 2*c - 1 != 0:

            nodeR = nodeL
            for i in range(n - 2*c - 1):
                nodeR = nodeR.next

            nodeR.next = nodeL.next
            nodeL.next = nodeR
            nodeL = nodeL.next.next
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
