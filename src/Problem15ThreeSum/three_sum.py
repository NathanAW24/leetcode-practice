from typing import List
from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                # to consider the case for [..., -3, -3,...], duplicate values being
                #                                     ^
                # when i is pointing there, since we have done the rest of the function with -3 as well previously
                # we don't need to do the same thing again here (we don't want duplicates)
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
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return res


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))

nums = [0, 1, 1]
print(Solution().threeSum(nums))

nums = [0, 0, 0]
print(Solution().threeSum(nums))

nums = [3, 0, -2, -1, 1, 2]
print(Solution().threeSum(nums))
