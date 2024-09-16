from typing import List


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


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))

prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
