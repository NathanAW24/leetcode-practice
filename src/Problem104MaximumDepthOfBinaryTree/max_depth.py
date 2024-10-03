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
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        max_count = 0

        if root is None:
            return 0

        stack = [(root, 1)]  # store (node, count)

        while stack:
            node, count = stack.pop()
            max_count = max(max_count, count)

            if node.right:
                stack.append((node.right, count+1))
            if node.left:
                stack.append((node.left, count+1))

        return max_count


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(12), TreeNode(7)))
print(Solution().maxDepth(root))
