# Problems
## Problem 1: TLE
With this `O(n^2)` algorithm, it return a TLE.
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for right in range(1, len(prices)):
            left = 0
            while left < right:
                profit = max(profit, prices[right] - prices[left])
                print(left, right, profit)
                left += 1
        return profit
```
