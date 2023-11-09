from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):  # only condition to return -1, bcs if >=, confirm there is a solution, just need to find the proper index
            return -1

        gain = 0
        idx = 0

        for i in range(len(gas)):
            gain += gas[i] - cost[i]

            if gain < 0:
                gain = 0
                idx = i + 1

        return idx


if __name__ == "__main__":
    solution = Solution()

    gas = [2, 3, 4]
    cost = [3, 4, 3]
    print(solution.canCompleteCircuit(gas, cost))

    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(solution.canCompleteCircuit(gas, cost))
