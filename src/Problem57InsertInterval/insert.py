from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i, interval in enumerate(intervals):
            # check if this interval merges with newInterval
            anchor_l, anchor_r = interval

            new_l, new_r = newInterval

            if new_r < anchor_l:  # newInterval is at the left of some interval at i
                print(
                    f"newInterval {newInterval} at the left of some interval {i} {interval}")
                result.append(newInterval)
                return result + intervals[i:]

            elif new_l > anchor_r:
                print(
                    f"newInterval {newInterval} is at the right of interval {i} {interval}, safely append the interval")

                result.append(interval)

            elif new_l <= anchor_l <= anchor_r <= new_r:
                print(
                    f"Yellow merge interval {interval} with newInterval {newInterval}")
                newInterval = [new_l, new_r]

            elif anchor_l <= new_l <= new_r <= anchor_r:
                print(
                    f"Pink merge interval {interval} with newInterval {newInterval}")
                newInterval = [anchor_l, anchor_r]

            elif new_l <= anchor_l <= new_r:
                print(
                    f"Red merge interval {interval} with newInterval {newInterval}")
                newInterval = [new_l, anchor_r]

            elif new_l <= anchor_r <= new_r:
                print(
                    f"Blue merge interval {interval} with newInterval {newInterval}")
                newInterval = [anchor_l, new_r]

            # elif new_r < anchor_l:  # newInterval is at the left of some interval at i
            #     print(
            #         f"newInterval {newInterval} at the left of some interval {i} {interval}")
            #     result.append(newInterval)

            # elif new_l > anchor_r:
            #     print(
            #         f"newInterval {newInterval} is beyond interval {i} {interval}, safely append the interval")

            #     result.append(interval)

            print(f'the newInterval is {newInterval}, result is {result}')

        result.append(newInterval)

        return result


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(Solution().insert(intervals, newInterval))

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(Solution().insert(intervals, newInterval))
