from collections import defaultdict


class Solution:
    def climbStairs(self, n: int) -> int:
        # dp_arr will be <no-steps-to-top> : <no-of-ways-to-reach-top>
        dp_arr = defaultdict(int)
        dp_arr[1] = 1  # base case 1
        dp_arr[2] = 2  # base case 2

        for i in range(3, n+1):
            dp_arr[i] = dp_arr[i-1] + dp_arr[i-2]

        return dp_arr[n]


n = 2
print(Solution().climbStairs(n))

n = 3
print(Solution().climbStairs(n))
