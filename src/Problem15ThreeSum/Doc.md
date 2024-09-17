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

Skip to neetcode solution, logic is very wrong from the beginning already

# Neetcode Solution
The key here is to sort `nums`, then iterate over the array once, for every element in the `nums` array. Then use the current `num`, then do two sum solution with two pointers `left` and `right` (since the array is sorted).

Here's the code with comments to explain why the line is written there.
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                # to consider the case for [..., -3, -3,...], duplicate values being
                #                                     ^
                # when i is pointing there, since we have done the rest of the function with -3 as well previously
                # we don't need to do the same thing again here (we don't want duplicates)
                continue

            # the rest is two pointer solution for sorted array for index [i+1, ..., n-1] inclusive
            # basically consider the values for the rest of the array after `i`
            # only need to consider after `i` as we don't want repeated indices or values selected againf
            left, right = i + 1, len(nums)-1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum > 0:  # 0 is `target`, can be changed to `target` given the right problem
                    right -= 1  # we need to reduce the sum, move `right` pointer left to reduce value of `three_sum`
                elif three_sum < 0:
                    left += 1  # we need to increase the sum, move 'left' pointer right to increase value of `three_sum`
                else:  # exactly eq to `target` `0`
                    res.append([num, nums[left], nums[right]])

                    left += 1  # move `left` pointer right, to avoid finding duplicates
                    while nums[left] == nums[left-1] and left < right:
                        # similar to check in the beginning
                        # to consider the case for [..., -3, -3,...], duplicate values
                        #                                     ^
                        # skip all duplicate values here
                        left += 1

        return res
```

FYI the last line should also work with moving the `right` pointer left.
```python
                    left += 1  # move `left` pointer right, to avoid finding duplicates
                    while nums[left] == nums[left-1] and left < right:
                        # similar to check in the beginning
                        # to consider the case for [..., -3, -3,...], duplicate values
                        #                                     ^
                        # skip all duplicate values here
                        left += 1
```
replace with
```python
                    right -= 1  # move `left` pointer right, to avoid finding duplicates
                    while nums[right] == nums[right+1] and left < right:
                        # similar to check in the beginning
                        # to consider the case for [..., -3, -3,...], duplicate values
                        #                                     ^
                        # skip all duplicate values here
                        right -= 1
```

So the code becomes
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                # to consider the case for [..., -3, -3,...], duplicate values being
                #                                     ^
                # when i is pointing there, since we have done the rest of the function with -3 as well previously
                # we don't need to do the same thing again here (we don't want duplicates)
                continue

            # the rest is two pointer solution for sorted array for index [i+1, ..., n-1] inclusive
            # basically consider the values for the rest of the array after `i`
            # only need to consider after `i` as we don't want repeated indices or values selected againf
            left, right = i + 1, len(nums)-1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum > 0:  # 0 is `target`, can be changed to `target` given the right problem
                    right -= 1  # we need to reduce the sum, move `right` pointer left to reduce value of `three_sum`
                elif three_sum < 0:
                    left += 1  # we need to increase the sum, move 'left' pointer right to increase value of `three_sum`
                else:  # exactly eq to `target` `0`
                    res.append([num, nums[left], nums[right]])

                    right -= 1  # move `left` pointer right, to avoid finding duplicates
                    while nums[right] == nums[right+1] and left < right:
                        # similar to check in the beginning
                        # to consider the case for [..., -3, -3,...], duplicate values
                        #                                     ^
                        # skip all duplicate values here
                        right -= 1

        return res
```