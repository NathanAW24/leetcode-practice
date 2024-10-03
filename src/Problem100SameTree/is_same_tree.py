from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # helpers

    def __str__(self):
        result = []
        stack = [self]  # Start with the root node

        while stack:
            current = stack.pop()
            if current:
                result.append(current.val)  # Visit the node
                stack.append(current.right)  # Push right child to stack
                stack.append(current.left)   # Push left child to stack

        return str(result)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is not None) or (q is None and p is not None):
            return False

        if p is None and q is None:
            return True

        stack_p = [p]
        stack_q = [q]

        while stack_p and stack_q:
            node_p = stack_p.pop()
            node_q = stack_q.pop()

            if node_p.val != node_q.val:
                return False

            if (node_p.right is None and node_q.right is not None) or (node_p.right is not None and node_q.right is None) or (node_p.left is None and node_q.left is not None) or (node_p.left is not None and node_q.left is None):
                # basically checking tree structure in upcoming direct children
                return False

            if node_p.right and node_q.right:
                stack_p.append(node_p.right)
                stack_q.append(node_q.right)

            if node_p.left and node_q.left:
                stack_p.append(node_p.left)
                stack_q.append(node_q.left)

        return True


p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().isSameTree(p, q))
