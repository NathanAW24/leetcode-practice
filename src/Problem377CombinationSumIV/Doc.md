# Idea of Solving
## Recursion can be used for this
Given a `target`, and a list of numbers `nums = [nums[0], ..., nums[n-1]]`. We can brute force add up the numbers until we reach the target.

Here's what we can do, for `i, j, k,... = 0, ..., n-1`

CASE 1: `nums[i] + nums[j] + nums[k] + ... = target` &rarr; add `+1` to `counter`.

OR

CASE 2: `nums[i] + nums[j] + nums[k] + ... > target` &rarr; break but no need to add anything.

OR 

CASE 3: `nums[i] + nums[j] + nums[k] + ... < target` &rarr; add more numbers `nums[l]` until it reaches CASE 1 or CASE 2

## Problems
# Problem 1: Wrong Logic
```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        counter = 0

        sum = 0

        def recursion(nums, target, sum, counter, arr_sum=[]):  # return integer
            if sum == target:
                # end recursion
                return counter + 1
            if sum > target:
                # end recursion
                return counter
            else:  # sum < target
                for i in range(len(nums)):
                    arr_sum.append(nums[i])
                    print('arr_sum ', arr_sum)
                    return recursion(nums, target, sum+nums[i], counter, arr_sum)

        return recursion(nums, target, sum, counter)

```

The loop is supposed to iterate over all number in `nums`, but since it returns inside the loop, with this line,
```python
                    return recursion(nums, target, sum+nums[i], counter, arr_sum)
```
we only receive the first iteration only.

This is the code fixed by ChatGPT
```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        sum = 0

        def recursion(nums, target, sum):  # return integer
            if sum == target:
                # end recursion
                return 1
            if sum > target:
                # end recursion
                return 0

            counter = 0
            for i in range(len(nums)):
                counter += recursion(nums, target, sum + nums[i])
            return counter

        return recursion(nums, target, sum)
```

A FEW NOTES
1. `sum + nums[i]` acts as the new sum of that ongoing iteration.
2. Why do we put the `counter = 0` within the `recursion` function, not outside? 
    - We don't want `counter` shared across recursive calls
    - What we want is a local `counter` for each sub-branch, as the sub-branches `counter` values will all be added in the top branch through `counter += recursion(nums, target, sum + nums[i])`, and returned afterwards `return counter`

Same logic but more readable code
```python
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
```

## Problem 2: TLE, need hashing
Before I hash
```python
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
```

Here is the new code with hashing, this passes leetcode solution.
```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        sum = 0
        hash = {}  # contains {sum: counter}

        def recursion(nums, target, sum):  # return integer
            if sum in hash:
                return hash[sum]
            elif sum == target:
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
                hash[sum] = counter
                return counter  # sum < target

        return recursion(nums, target, sum)
```

## Problem 3: Function looks nasty AF NGL
This is the initial way it looks
```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        sum = 0
        hash = {}  # contains {sum: counter}

        def recursion(nums, target, sum):  # return integer
            if sum in hash:
                return hash[sum]
            elif sum == target:
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
                hash[sum] = counter
                return counter  # sum < target

        return recursion(nums, target, sum)
```

Just need to make it neater by separating both functions
```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        sum = 0
        hash = {}  # contains {sum: counter}

        return self.recursion(nums, target, sum, hash)

    def recursion(self, nums, target, sum, hash):  # return integer
        if sum in hash:
            return hash[sum]
        elif sum == target:
            # end recursion
            return 1
        elif sum > target:
            # end recursion
            return 0
        else:
            counter = 0
            # all addition procedure for the `counter` lies here
            for i in range(len(nums)):
                counter += self.recursion(nums, target, sum + nums[i], hash)

            # it is finished adding all values for `counter`
            hash[sum] = counter
            return counter  # sum < target
```