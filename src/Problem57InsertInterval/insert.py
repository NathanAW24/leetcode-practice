from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i, interval in enumerate(intervals):
            # check if this interval merges with newInterval
            anchor_l, anchor_r = interval

            new_l, new_r = newInterval

            if new_l <= anchor_l <= anchor_r <= new_r:
                print(
                    f"Yellow merge interval {interval} with newInterval {newInterval}")
                newInterval = [new_l, new_r]
                result.append(newInterval)

            elif anchor_l <= new_l <= new_r <= anchor_r:
                print(
                    f"Pink merge interval {interval} with newInterval {newInterval}")
                newInterval = [anchor_l, anchor_r]
                result.append(newInterval)

            elif new_l <= anchor_l <= new_r:
                print(
                    f"Red merge interval {interval} with newInterval {newInterval}")
                newInterval = [new_l, anchor_r]
                result.append(newInterval)

            elif new_l <= anchor_r <= new_r:
                print(
                    f"Blue merge interval {interval} with newInterval {newInterval}")
                newInterval = [anchor_l, new_r]
                result.append(newInterval)

            else:  # no intervals at all
                print(
                    f"NO merge, interval {interval} with newInterval {newInterval}")
                result.append(interval)

            print(f'the newInterval is {newInterval}')

        return result


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(Solution().insert(intervals, newInterval))

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(Solution().insert(intervals, newInterval))
