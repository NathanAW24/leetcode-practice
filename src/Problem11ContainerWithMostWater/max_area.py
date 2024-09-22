from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        right = n-1
        left = 0

        while left < right:
            max_area = max(
                min(height[left], height[right]) * (right-left), max_area)

            if height[left] <= height[right]:  # right as anchor
                left += 1
            else:  # left as anchor
                right -= 1

        return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))

height = [1, 1]
print(Solution().maxArea(height))
