# Scribbles
## Scribble 1
```
1
```
`(1).next == None` &rarr; `(1)` is head and tail &rarr; return `(1)` basically same node

## Scribble 2

```
1 -> 2
```
`(1).next != None` &rarr; `(1).next => (2)`
    `(2).next == None` &rarr; `(2).next = (1)` then `(2).next => (1)`
    `(1).next = None`


## Scribble 3
```
1 -> 2 -> 3
```
`(1).next != None` &rarr; `(1).next => (2)`, then set `[1].next = {None}`
    `(2).next != None` &rarr; `(2).next => (3)`, then set `[2].next = {1}`
        `(3).next == None` (BASE CASE) &rarr; `(3).next => (None)`, then set `[3].next = {2}`

# My Solution (Without Looking at Neetcode)
Based on Scribble 3, there are three pointers that needs to be set here, which is `(node1)`, `[node2]`, and `{nodePrev}`. `(node1)` is tasked as the main mover within the array. `[node2]` is tasked to reverse the node's `.next` value to the value before. `{nodePrev}` is used to store the value before, which is later assigned by `[node2]`.

Then basically in each loop we should assign `{nodePrev}` as previous node (which is going to be new `.next`, when reversed). `[node2]` as current node (in `(node1)`). `(node1)` as the next possible value within the linked list, to move the progression of the main pointer.

```python
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

        while node1.next != None:
            nodePrev = None if node1 == head else node2

            node2 = node1

            node1 = node1.next

            node2.next = nodePrev
            # print(f'nodePrev: {nodePrev}, node1: {node1}, node2: {node2}')

        # don't forget to set the final node, to the node2
        node1.next = node2
        # print(f'nodePrev: {nodePrev}, node1: {node1}, node2: {node2}')

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
```

Also made a checker function for testing purposes.