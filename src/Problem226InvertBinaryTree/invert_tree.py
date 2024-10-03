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

    def build_bst_from_inorder_list(self, values):
        if not values:
            return None

        return self.build_bst_from_inorder_list_helper(values, 0, len(values) - 1)

    def build_bst_from_inorder_list_helper(self, values, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        root = TreeNode(values[mid])
        root.left = self.build_bst_from_inorder_list_helper(
            values, start, mid - 1)
        root.right = self.build_bst_from_inorder_list_helper(
            values, mid + 1, end)

        return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # pre-order traversal
        if root is None or (root.left is None and root.right is None):
            return root

        stack = [root]

        while stack:  # stack is not empty
            node = stack.pop()
            # check for switching
            if node.left or node.right:
                tmp = node.left
                node.left = node.right
                node.right = tmp

            # check if right and left is not None, nodes are switched
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(7, TreeNode(6), TreeNode(9)))
print(Solution().invertTree(root))
