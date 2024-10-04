from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # (candidate, sum-including-candidate, [...candidates-used])
        stack = [(0, 0, [])]
        results = []

        # count = 0

        # for candidate in candidates:
        #     stack.append((candidate, count + candidate, [candidate]))

        # print(stack)

        while stack:
            prev_candidate, prev_count, prev_candidates_used = stack.pop()

            for curr_candidate in candidates:
                curr_count = prev_count + curr_candidate

                if len(prev_candidates_used) >= 1 and prev_candidates_used[-1] > curr_candidate:
                    continue

                if curr_count > target:
                    continue
                    # print(f"run stack pop, {curr_count} > 7")
                    # stack.pop()  # this is the value with curr_count > 7, don't need to continue counting again, and is done after appending
                elif curr_count == target:
                    # print(
                    #     f"run curr_count == 7, {[*prev_candidates_used, curr_candidate]}")
                    # stack.pop()  # also pop if its 7, coz no longer need to count, but can just append to results
                    results.append([*prev_candidates_used, curr_candidate])
                else:  # < 7
                    stack.append((curr_candidate, curr_count, [
                                 *prev_candidates_used, curr_candidate]))

            # print(stack)

        return results


candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))

candidates = [2, 3, 5]
target = 8
print(Solution().combinationSum(candidates, target))

candidates = [2]
target = 1
print(Solution().combinationSum(candidates, target))
