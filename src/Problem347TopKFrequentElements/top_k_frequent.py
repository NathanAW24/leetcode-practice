from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # track for key (the num inside nums) : value (number of appearances)
        hash = defaultdict(lambda: 0)  # default value be 0

        for num in nums:
            hash[num] += 1

        return sorted(hash.keys(), key=lambda hash_key: hash[hash_key], reverse=True)[0:k]


# test case 1
nums = [2, 2, 3, 5, 5, 5]
k = 2
print(Solution().topKFrequent(nums, k))

# test case 2
nums = [1]
k = 1
print(Solution().topKFrequent(nums, k))
