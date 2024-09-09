from typing import List
from collections import defaultdict


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            if i > 0:
                prefix = prefix * nums[i-1]
            output[i] = output[i] * prefix

        postfix = 1
        for i in range(n-1, -1, -1):
            if i < n-1:
                postfix = postfix * nums[i+1]
            output[i] = output[i] * postfix

        return output


# test case 1
nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))

# test case 2
nums = [-1, 1, 0, -3, 3]
print(Solution().productExceptSelf(nums))
