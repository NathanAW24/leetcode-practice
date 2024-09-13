from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        sum = 0

        def recursion(nums, target, sum):  # return integer
            if sum == target:
                # end recursion
                return 1
            elif sum > target:
                # end recursion
                return 0
            else:
                counter = 0
                # all addition procedure for the `counter` lies here
                for i in range(len(nums)):
                    counter += recursion(nums, target, sum + nums[i])

                # it is finished adding all values for `counter`
                return counter  # sum < target

        return recursion(nums, target, sum)


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
