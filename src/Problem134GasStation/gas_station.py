from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        gain = 0
        idx = 0

        for i in range(len(gas)):
            gain += gas[i] - cost[i]
            total_gain += gas[i] - cost[i]

            if gain < 0:
                gain = 0
                idx = i + 1

        return idx if total_gain >= 0 else -1


if __name__ == "__main__":
    solution = Solution()

    gas = [2, 3, 4]
    cost = [3, 4, 3]
    print(solution.canCompleteCircuit(gas, cost))

    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(solution.canCompleteCircuit(gas, cost))
