
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False


nums = [1, 2, 3, 1]
solution1 = Solution()
print(solution1.containsDuplicate(nums))

nums = [1, 2, 3, 4]
solution1 = Solution()
print(solution1.containsDuplicate(nums))

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
solution1 = Solution()
print(solution1.containsDuplicate(nums))
