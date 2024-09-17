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

            # the rest is two pointer solution for sorted array for index [i+1, ..., n-1] inclusive
            # basically consider the values for the rest of the array after `i`
            # only need to consider after `i` as we don't want repeated indices or values selected againf
            left, right = i + 1, len(nums)-1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum > 0:  # 0 is `target`, can be changed to `target` given the right problem
                    right -= 1  # we need to reduce the sum, move `right` pointer left to reduce value of `three_sum`
                elif three_sum < 0:
                    left += 1  # we need to increase the sum, move 'left' pointer right to increase value of `three_sum`
                else:  # exactly eq to `target` `0`
                    res.append([num, nums[left], nums[right]])

                    right -= 1  # move `left` pointer right, to avoid finding duplicates
                    while nums[right] == nums[right+1] and left < right:
                        # similar to check in the beginning
                        # to consider the case for [..., -3, -3,...], duplicate values
                        #                                     ^
                        # skip all duplicate values here
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
