from collections import defaultdict
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = 1  # arr-idx : max-value-from-0-to-i-inc
        dp_min = 1  # arr-idx: min-value-from-0-to-i-inc
        max_num = max(nums)

        for i in range(len(nums)):
            if i == 0:
                dp_max = nums[i]
                dp_min = nums[i]
            else:
                temp_dp_max_calc = dp_max * nums[i]
                dp_max = max(temp_dp_max_calc,
                             dp_min * nums[i], nums[i])
                dp_min = min(temp_dp_max_calc,
                             dp_min * nums[i], nums[i])
            max_num = max(dp_max, max_num)

        return max_num


nums = [2, 3, -2, 4]
print(Solution().maxProduct(nums))

nums = [2, 0, 3, -2, 4]
print(Solution().maxProduct(nums))

nums = [-2, 0, -1]
print(Solution().maxProduct(nums))
