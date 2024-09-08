# Problems
## Problem 1: Time Limit Exceeded
The most stupid solution is to run it in `O(n^2)`.
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # start of with O(n^2) solution
        res = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    res[i] *= nums[j]

        return res
```

So we need to find another solution.
