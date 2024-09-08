from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # start of with O(n^2) solution
        res = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    res[i] *= nums[j]

        return res


# test case 1
nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))

# test case 2
nums = [-1, 1, 0, -3, 3]
print(Solution().productExceptSelf(nums))
