# Thought Process
This one not so difficult also, just traverse in the same way, then compare one by one.
```python
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

```