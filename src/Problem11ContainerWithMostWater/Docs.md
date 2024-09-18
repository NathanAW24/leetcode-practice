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

Sliding window start from `left=0` and `right=1`, the main loop has a functionality of moving the `right` pointer to the right, iterating from beginning to end of the array. While, the `left` pointer only be moved when it satisfies a certain condition, to the right as well. ChatGPT says, sliding window is only used when..
- When you are focusing on a **single range** that moves **left to right**. You only care about the **range or window size** and the **values inside that range** (e.g., sum, difference, max, etc.). You often move **both ends of the window independently** (not in sync), but in **one direction** (typically from left to right).

Sliding Window Generalization:
- **Contiguous subarray or sequence**: Analyzing or optimizing values within continugous range or window in the array.
- **Fixed order matters**: Care about the sequence in which the elements appear, must buy before selling the stock.
- **Tracking a value as the window changes**: Continuously updating and tracking  value, as the sliding window slides across the array.

This problem requires two pointers, `left=0` and `right=n-1`, the main loop would move the `left` or `right` pointer depending on the values of the array at `left` or `right`, the movement goes two directions, so it normally goes inwards from both ends. ChatGPT says it is used when...
-  When the solution requires working with **two elements or ranges simultaneously**. Often used when you need to **shrink the problem from both ends**, which involves two moving pointers that can adjust dynamically. The two pointers often move **towards each other** or stay far apart while reducing the problem space (usually to find something like a max/min combination or balance).

Two Pointers Generalization:
- **Comparing elements or combinations**: You are comparing two elements or values that may be far apart and adjusting them based on conditions.
- **Optimizing combinations of two elements**: Trying to find optimal result from two different elements, and moving one pointer inward won't affect feasibility of the other. In the beginning might seem to need all combinations of the elements, but there's a logical loophole that can be used along with the two pointer solution.