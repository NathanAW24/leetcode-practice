# Thought Process
## When is the right pointer moved?
`max_pr = 0`
```
2 3 -2 4
^
l,r
```
`pr = nums[l] * ... * nums[r] = 2`


```
2 3 -2 4
^ ^
l r
```
`pr = nums[l] * ... * nums[r] = prev_pr * nums[r] = 2 * 3 = 6`
`max_pr = 6`

```
2 3 -2 4
^ ^
l r
```


# Neetcode
The key here is to keep a `dp_min` and `dp_max` multiplication value at every iteration. The reason here is because, the `max_num` value can be gotten by multiplying a very negative `dp_min` with another negative number. 

Both the max and min values can be retrieved by comparing the values of `dp_max * nums[i]`, `dp_min * nums[i]`, and `nums[i]`, this is because, the `dp_min`, `dp_max` and `nums[i]` can be positive or negative, thus we must compare everything to find the greatest result. If only `nums[i]` is selected, means its a product of the subarray that start at `nums[i]`. When `dp_min` and `dp_max` is `0` is considered here as well, then the `nums[i]`, would be chosen when it is positive. So, that case is handled as well.
```python
...
                temp_dp_max_calc = dp_max * nums[i]
                dp_max = max(temp_dp_max_calc,
                             dp_min * nums[i], nums[i])
                dp_min = min(temp_dp_max_calc,
                             dp_min * nums[i], nums[i])
...
```

![alt text](image.png)

Here's the full code
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = 1  # arr-idx : max-value-from-0-to-i-inc
        dp_min = 1  # arr-idx: min-value-from-0-to-i-inc
        max_num = max(nums)

        for i in range(len(nums)):
            if i == 0:
                dp_max = nums[i]
                dp_min = nums[i]
            else:
                temp_dp_max_calc = dp_max * nums[i]
                dp_max = max(temp_dp_max_calc,
                             dp_min * nums[i], nums[i])
                dp_min = min(temp_dp_max_calc,
                             dp_min * nums[i], nums[i])
            max_num = max(dp_max, max_num)

        return max_num
```