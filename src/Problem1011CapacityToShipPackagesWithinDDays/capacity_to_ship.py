from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def traversePossible(self, weights: List[int], mid) -> bool:
            # nathan
            ship_i_weight = 0
            ship = 1

            i = 0

            for weight in weights:
                ship_i_weight += weight

                if ship_i_weight > mid:
                    ship += 1
                    ship_i_weight = 0 + weight

                # print(f"at weight {weight} ship_{i}_weight is {ship_i_weight} no of ships {ship}")
                i += 1

            # true if ship needed less than or eq to number of ships allowed
            return True if ship <= days else False

        L, R = max(weights), sum(weights)
        res = R

        while L <= R:
            mid = (L + R) // 2  # value of mid enough for carrying each weight in one ship\
            # print(f"L is {L} R is {R}")
            # print(f"mid is {mid}")

            canTraverse = traversePossible(self, weights, mid)
            # print(canTraverse)

            if canTraverse:
                R = mid - 1  # lower mid
                res = min(res,  mid)
            else:
                L = mid + 1  # increase mid

        return res


if __name__ == "__main__":
    solution = Solution()

    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    print(solution.shipWithinDays(weights, days))

    weights = [3, 2, 2, 4, 1, 4]
    days = 3
    print(solution.shipWithinDays(weights, days))

    weights = [1, 2, 3, 1, 1]
    days = 4
    print(solution.shipWithinDays(weights, days))
