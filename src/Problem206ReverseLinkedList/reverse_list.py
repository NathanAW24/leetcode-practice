from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(f"val {self.val}, next {self.next.val if self.next != None else None}")


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return head

        if head.next == None:
            return head

        node1 = head
        node2 = None

        while node1.next != None:
            nodePrev = node2

            node2 = node1

            node1 = node1.next

            node2.next = nodePrev

        # don't forget to set the final node, to the node2
        node1.next = node2

        return node1

    def checker(self, head):

        node = self.reverseList(head)

        while node.next != None:
            print(node)
            node = node.next


nodeFive = ListNode(5)
nodeFour = ListNode(4, nodeFive)
nodeThree = ListNode(3, nodeFour)
nodeTwo = ListNode(2, nodeThree)
nodeOne = ListNode(1, nodeTwo)
Solution().checker(nodeOne)
