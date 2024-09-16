from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        right = 1  # buy
        left = 0  # sell

        while right < len(prices):
            if prices[right] - prices[left] > 0:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:  # sell is smaller than buy, malah rugi, means there's a better value in the future to buy from, which will confirm yield to greater profit than if we kept the left value to current
                left = right

            right += 1

        return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))

prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
