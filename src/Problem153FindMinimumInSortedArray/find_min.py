from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1
        mid = (r-l)//2 + l

        if len(nums) == 1:
            return nums[0]  # smallest number be the only number itself

        if nums[l] < nums[r]:
            return nums[0]

        while l != mid:
            if nums[l] > nums[mid]:
                # choose left
                r = mid
            elif nums[mid] > nums[r]:
                l = mid

            mid = (r-l)//2 + l

            print(f"l, mid, r: {l, mid, r}")

        return nums[l+1]


nums = [3, 4, 5, 1, 2]
print(Solution().findMin(nums))

nums = [4, 5, 6, 7, 0, 1, 2]
print(Solution().findMin(nums))

nums = [11, 13, 15, 17]
print(Solution().findMin(nums))

nums = [15, 17, 11, 13]
print(Solution().findMin(nums))
