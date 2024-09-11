from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxlength = 0

        for num in nums:
            if num-1 not in numSet:  # start of sequence
                length = 1
                while num+length in numSet:  # not end of sequence
                    length += 1
                # reached the end of sequence, whether is it the same number or not
                maxlength = max(length, maxlength)
            # num-1 in numSet means it is not start of sequence and we can ignore it

        return maxlength


nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(nums))

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(Solution().longestConsecutive(nums))
