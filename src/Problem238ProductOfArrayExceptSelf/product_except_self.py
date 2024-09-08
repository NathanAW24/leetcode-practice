from typing import List
from collections import defaultdict


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        postfix = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            if i > 0:  # after first element
                prefix[i] = prefix[i-1] * nums[i]
            else:
                prefix[i] = nums[i]

        for i in range(len(nums)-1, -1, -1):
            if i >= len(nums) - 1:
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i] * postfix[i+1]

        res = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i <= 0:
                res[i] = postfix[i+1]
            elif i >= len(nums)-1:
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * postfix[i+1]
        return res


# test case 1
nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))

# test case 2
nums = [-1, 1, 0, -3, 3]
print(Solution().productExceptSelf(nums))
