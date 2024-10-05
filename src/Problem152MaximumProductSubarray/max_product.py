from collections import defaultdict
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = {}  # arr-idx : max-value-from-0-to-i-inc
        dp_min = {}  # arr-idx: min-value-from-0-to-i-inc
        max_num = max(nums)

        for i in range(len(nums)):
            if i == 0:
                dp_max[i] = nums[i]
                dp_min[i] = nums[i]
            else:
                dp_max[i] = max(dp_max[i-1] * nums[i],
                                dp_min[i-1] * nums[i], nums[i])
                dp_min[i] = min(dp_max[i-1] * nums[i],
                                dp_min[i-1] * nums[i], nums[i])
            max_num = max(dp_max[i], max_num)

        return max_num


nums = [2, 3, -2, 4]
print(Solution().maxProduct(nums))

nums = [2, 0, 3, -2, 4]
print(Solution().maxProduct(nums))

nums = [-2, 0, -1]
print(Solution().maxProduct(nums))
