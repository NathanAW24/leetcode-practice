# Thought Process
Problem was quite easy, not need a lot of time to resolve tbh. Basically logical thought process was just to traverse pre-order
```python
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
```