from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        noOfPrefixSumHash = {}  # {prefixSum: {how many times prefixSum appears}}
        count = 0
        subSum = 0

        for i in range(len(nums)):
            subSum = 0
            for j in range(i, len(nums)):
                subSum = subSum + nums[j]
                if subSum == k:
                    count += 1

        return count


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 4, 2, 2, 1]
    k = 4
    print("Test Case 1")
    print(solution.subarraySum(nums, k))
    nums = [1, 1, 1]
    k = 2
    print("Test Case 2")
    print(solution.subarraySum(nums, k))
    nums = [1, 2, 3]
    k = 3
    print("Test Case 3")
    print(solution.subarraySum(nums, k))
