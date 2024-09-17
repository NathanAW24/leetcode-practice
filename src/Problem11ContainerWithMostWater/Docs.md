# Problems
## Problem 1: Thinking it's Similar to Stocks Problem 121
Asked ChatGPT why these two problems are different.

Why Sliding Window (in Leetcode 121) Doesn’t Work for Leetcode 11?
- In Leetcode 11, moving one pointer and resetting it (as you do in a sliding window) won't help, because the maximum area **requires the optimal distance between the pointers**. Simply resetting the pointer based on whether one side is lower doesn't give you the full picture of the area potential.
- In Leetcode 121, you’re only looking for the largest profit (**difference between two points**), which means once you’ve found a lower price, you can effectively **ignore previous points**. In Leetcode 11, however, both pointers always matter because you need to consider the area formed between the current two heights.

That's why this code doesn't work
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        right = 1
        left = 0

        while right < len(height):
            curr_max_area = max(
                min(height[left], height[right]) * (right-left), max_area)
            if curr_max_area > max_area:
            right += 1
                left = right
                max_area = curr_max_area
        return curr_max_area
```
