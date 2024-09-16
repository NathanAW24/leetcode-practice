from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}  # {value: index}

        for idx, number in enumerate(nums):
            if target - number in hash:
                return [hash[target - number], idx]
            else:
                hash[number] = idx
        return


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))

nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target))

nums = [3, 3]
target = 6
print(Solution().twoSum(nums, target))
