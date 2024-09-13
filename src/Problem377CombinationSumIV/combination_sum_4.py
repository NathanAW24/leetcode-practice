from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        sum = 0
        hash = {}

        return self.recursion(nums, target, sum, hash)

    def recursion(self, nums, target, sum, hash):
        if sum in hash:
            return hash[sum]
        elif sum == target:
            return 1
        elif sum > target:
            return 0
        else:
            counter = 0
            for i in range(len(nums)):
                counter += self.recursion(nums, target, sum + nums[i], hash)

            hash[sum] = counter
            return counter


nums, target = [1, 2, 3], 4
print(Solution().combinationSum4(nums, target))

nums, target = [9], 3
print(Solution().combinationSum4(nums, target))

''' 
CASE FOR nums, target = [1, 2, 3], 4

counter = 0

nums[i] being summed, sum
1,1 --> call: counter += recursion(...) (all nums[i])

------------------------------
1 1, 2 --> call: counter += recursion(...) (all nums[i]) --> counter += 1 + 1 + 0 --> counter = 2 --> return counter
--------------------
1 1 1, 3 --> call: counter += recursion(...) (all nums[i]) --> counter += 1 + 0 + 0 --> counter = 1 --> return counter
----------
1 1 1 1, 4 --> return 1
1 1 1 2, 5 --> return 0
1 1 1 3, 6 --> return 0
----------


1 1 2, 4 --> return 1
1 1 3, 5 --> return 0
--------------------

1 2, 3 --> call: counter += recursion(...) (all nums[i]) --> counter += ...

...

------------------------------

'''
