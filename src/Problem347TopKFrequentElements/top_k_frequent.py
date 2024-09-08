from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # track for key (the num inside nums) : value (number of appearances)
        hash = defaultdict(lambda: 0)  # default value be 0

        for num in nums:
            hash[num] += 1

        sorted_key_value_pair = sorted(
            hash.items(), key=lambda item: item[1], reverse=True)

        return [sorted_key_value_pair[i][0] for i in range(0, k)]


# test case 1
nums = [2, 2, 3, 5, 5, 5]
k = 2
print(Solution().topKFrequent(nums, k))

# test case 2
nums = [1]
k = 1
print(Solution().topKFrequent(nums, k))
