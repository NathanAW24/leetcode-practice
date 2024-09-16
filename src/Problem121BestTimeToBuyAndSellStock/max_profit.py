from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        right = 1
        left = 0

        while right < len(prices):
            if prices[right] - prices[left] > 0:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right

            right += 1

        return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))

prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
