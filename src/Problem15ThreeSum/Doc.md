# Problems
## Problem 1: They want distinct values where order doesn't matter
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash = {}  # record { nums[i] + nums[j]: [i,j]}
        # then do nums[k] + hash[...] = 0

        result = []

        n = len(nums)
        # record first
        for i in range(n):
            for j in range(n):
                if i != j:
                    hash[nums[i] + nums[j]] = [i, j]

        # do iteration one more time
        for k in range(n):
            if 0 - nums[k] in hash:
                i, j = hash[-nums[k]]
                if i != k and j != k:
                    result.append([nums[i], nums[j], nums[k]])

        return result


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
```

For the code and test case, it results in `[[-1, 2, -1], [-1, 1, 0], [-1, 0, 1]]`, but the wanted value is `[[-1, 2, -1], [-1, 1, 0]]` only, as they want distinct values, and the order doesn't matter. 

ChatGPT gave me a suggestion to use some data structures and strategies to make it easier to settle.
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash = {}  # record { nums[i] + nums[j]: [i,j]}
        # then do nums[k] + hash[...] = 0

        result = set()

        n = len(nums)
        # record first
        for i in range(n):
            for j in range(n):
                if i != j:
                    hash[nums[i] + nums[j]] = [i, j]

        # do iteration one more time
        for k in range(n):
            if 0 - nums[k] in hash:
                i, j = hash[-nums[k]]
                if i != k and j != k:
                    sorted_triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(sorted_triplet)

        return [list(sorted_triplet) for sorted_triplet in result]
```

It helps that issue.

## Problem 2: Multiple Pairs sum to the same value, will overwrite `hash[key]`
The problem is in this part.
```python
...
        # record first
        for i in range(n):
            for j in range(n):
                if i != j:
                    hash[nums[i] + nums[j]] = [i, j]
...
```

In this case, if we do `hash[nums[i] + nums[j]] = [i, j]`, in array `[-1, 1, -2, 2]` when `i = 0` and `j = 1`, `nums[i] + nums[j] = 0`, same as when `i = 2` and `j = 3`, it will overwrite the value of `hash[nums[i] + nums[j]] = [i, j]` from `[0, 1]` to `[2, 3]`, but we want both.

So here's what I did
```python
...
        # record first
        for i in range(n):
            for j in range(n):
                if i != j:
                    hash[nums[i] + nums[j]] = [*hash[nums[i] + nums[j]], [i, j]]
...
```

## Problem 3: TLE
This code updated is TLE still
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash = defaultdict(list)  # record { nums[i] + nums[j]: [i,j]}
        # then do nums[k] + hash[...] = 0

        result = set()

        n = len(nums)
        # record first
        for i in range(n):
            for j in range(n):
                if i != j:
                    hash[nums[i] + nums[j]] = [*hash[nums[i] + nums[j]], [i, j]]

        # do iteration one more time
        for k in range(n):
            if 0 - nums[k] in hash:
                i_j_arrays = hash[-nums[k]]
                for i, j in i_j_arrays:
                    if i != k and j != k:
                        sorted_triplet = tuple(
                            sorted([nums[i], nums[j], nums[k]]))
                        result.add(sorted_triplet)

        return [list(sorted_triplet) for sorted_triplet in result]
```

Skip to neetcode solution

# Neetcode Solution