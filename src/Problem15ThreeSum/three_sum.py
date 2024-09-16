from typing import List
from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash = defaultdict(list)  # record { nums[i] + nums[j]: [i,j]}
        # then do nums[k] + hash[...] = 0

        result = set()

        n = len(nums)
        # record first
        for i in range(n):
            for j in range(n):
                if i != j:
                    hash[nums[i] + nums[j]] = [*hash[nums[i] + nums[j]], [i, j]]

        # do iteration one more time
        for k in range(n):
            if 0 - nums[k] in hash:
                i_j_arrays = hash[-nums[k]]
                for i, j in i_j_arrays:
                    if i != k and j != k:
                        sorted_triplet = tuple(
                            sorted([nums[i], nums[j], nums[k]]))
                        result.add(sorted_triplet)

        return [list(sorted_triplet) for sorted_triplet in result]


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))

nums = [0, 1, 1]
print(Solution().threeSum(nums))

nums = [0, 0, 0]
print(Solution().threeSum(nums))

nums = [3, 0, -2, -1, 1, 2]
print(Solution().threeSum(nums))
