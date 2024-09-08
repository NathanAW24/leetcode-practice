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

# Neetcode Solution
## Solution V1
use a `prefix` and `postfix` arrays, where `prefix[i] = prefix[0] * ... * prefix[i])` and `postfix[i] = postfix[i] * ... * postfix[n-1]`. Then, `result[i] = prefix[i-1] * postfix[i+1]`. I want to code this solution out first.
![alt text](image.png)

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            if i > 0:  # after first element
                prefix[i] = prefix[i-1] * nums[i]
            else:
                prefix[i] = nums[i]

        for i in range(len(nums)-1, -1, -1):
            if i >= len(nums) - 1:
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i] * postfix[i+1]

        res = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            if i <= 0:
                res[i] = postfix[i+1]
            elif i >= len(nums)-1:
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * postfix[i+1]
        return res
```

This solution runs, but can still be optimized for `O(1)` memory.
