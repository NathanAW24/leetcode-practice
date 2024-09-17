from typing import List
from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue

            left, right = i + 1, len(nums)-1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])

                    right -= 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1

        return res


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))

nums = [0, 1, 1]
print(Solution().threeSum(nums))

nums = [0, 0, 0]
print(Solution().threeSum(nums))

nums = [3, 0, -2, -1, 1, 2]
print(Solution().threeSum(nums))
