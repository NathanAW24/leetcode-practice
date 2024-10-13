from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i, interval in enumerate(intervals):

            anchor_l, anchor_r = interval
            new_l, new_r = newInterval

            if new_r < anchor_l:
                result.append(newInterval)
                return result + intervals[i:]

            elif new_l > anchor_r:
                result.append(interval)

            else:
                newInterval = [min(new_l, anchor_l), max(new_r, anchor_r)]

        result.append(newInterval)

        return result


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(Solution().insert(intervals, newInterval))

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(Solution().insert(intervals, newInterval))
