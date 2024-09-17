from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        right = 1
        left = 0

        while right < len(height):
            curr_max_area = max(
                min(height[left], height[right]) * (right-left), max_area)
            if curr_max_area > max_area:
                left = right
                max_area = curr_max_area
            right += 1
        return curr_max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))

height = [1, 1]
print(Solution().maxArea(height))
