from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # track for key (the num inside nums) : value (number of appearances)
        hash = defaultdict(lambda: 0)  # default value be 0
        counts = [[]] * (len(nums)+1)  # default value be []

        for num in nums:
            hash[num] += 1

        print(hash.items())
        for num, count in hash.items():
            print(count)
            print(counts[count])
            counts[count].append(num)
            print(counts)

        res = []
        for i in range(len(nums), -1, -1):
            # i start from n
            # counts[i] is a list
            for num in counts[i]:
                res.append(num)

        print(counts)
        print(res)


# test case 1
nums = [2, 2, 3, 5, 5, 5]
k = 2
print(Solution().topKFrequent(nums, k))

# test case 2
nums = [1]
k = 1
print(Solution().topKFrequent(nums, k))
