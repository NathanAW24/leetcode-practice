from typing import List


class Solution:
    # def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
    #     global ori_sums
    #     num_r, num_c = len(grid), len(grid[0])

    #     max_val = num_c // 2
    #     print(f"max_val {max_val}")
    #     ori_sums = [0, 0, 0]
    #     ori_idx = []

    #     def name(i, sums, idx):
    #         global ori_sums
    #         new_sums = sums[:]
    #         new_idx = idx[:]
    #         # try adding all into the sums first
    #         print(f"new_sums is {new_sums}")
    #         for j in range(num_c):
    #             new_sums[j] = new_sums[j] + grid[i][j]
    #         sums = new_sums[:]

    #         # check if im at last row
    #         if i + 1 >= num_r:
    #             print("last line")
    #             if any(num > max_val for num in sums):
    #                 print(f"to big, dismissing {i} row, {sums}")
    #                 return
    #             else:
    #                 print(f"ok, can take {i}, row, {sums}")
    #                 new_idx.append(i)
    #                 ori_idx = new_idx[:]
    #                 ori_sums = [*new_sums]
    #                 return
    #         else:  # can stil go next, not last row
    #             print("Can go next")
    #             if any(num > max_val for num in sums):
    #                 print(f"to big, dismissing {i} row, {sums}")
    #                 return  # no need to call next row as this thing is obsolete already
    #             else:
    #                 print(f"ok, can take {i}, row, {sums}")
    #                 new_idx.append(i)
    #                 name(i + 1, sums, new_idx)

    #         return

    #     name(0, ori_sums, ori_idx)
    #     return ori_sums
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        kamus = {}
        num_r, num_c = len(grid), len(grid[0])

        for i, row in enumerate(grid):
            num_value = 0
            power = 0
            for value in row[::-1]:
                # value 1 or 0, basically for row [1,0,1,0,1] ==> find numeric representaiton of the numnber
                num_value += value * (2**power)
                power += 1
            # store in the dict {numeric_rep_of_row: row_index}
            kamus[num_value] = i

        for i in range(32):  # here 32 bcs max col ada 5 doang
            if i in kamus:
                if i == 0:
                    # just pick the index with all zeros row, easiest valid, rmb u dont need to get the max
                    return [kamus[i]]
                else:
                    for j in range(32):
                        # now take the comparator
                        if j in kamus:
                            if i & j == 0:  # i and j same number
                                res = [kamus[i], kamus[j]]
                                if kamus[j] < kamus[i]:
                                    res = [kamus[j], kamus[i]]
                                return res

        return []


if __name__ == "__main__":
    solution = Solution()

    grid = [
        [0, 1, 0],
        [1, 1, 1],
        [1, 0, 0],
        [0, 0, 0],
    ]
    print(solution.goodSubsetofBinaryMatrix(grid))

    # grid = [
    #     [0, 0, 1, 0],
    #     [1, 1, 1, 1],
    #     [1, 0, 0, 0],
    # ]
    # print(solution.goodSubsetofBinaryMatrix(grid))

    # # gpt generated
    # grid = [
    #     [1, 0, 0, 0, 1, 0, 1, 0]
    #     [0, 0, 1, 0, 0, 0, 0, 1]
    #     [0, 1, 1, 0, 0, 0, 0, 0]
    #     [0, 0, 0, 0, 0, 1, 1, 1]
    #     [1, 0, 0, 0, 1, 0, 0, 0]
    # ]
    # print(solution.goodSubsetofBinaryMatrix(grid))

    # grid = [
    #     [1, 0, 1, 1, 1, 1, 1, 1]
    #     [0, 0, 0, 0, 0, 0, 0, 1]
    #     [0, 1, 1, 0, 0, 0, 0, 1]
    #     [0, 0, 0, 0, 0, 1, 1, 1]
    #     [1, 1, 1, 1, 1, 1, 0, 1]
    # ]
    # print(solution.goodSubsetofBinaryMatrix(grid))

    # grid = [
    #     [1, 0, 0, 1, 0, 1, 0, 1]
    #     [0, 1, 0, 1, 1, 0, 0, 0]
    #     [0, 0, 1, 1, 0, 0, 1, 1]
    #     [1, 1, 1, 0, 0, 1, 1, 0]
    #     [0, 1, 0, 0, 0, 1, 0, 0]
    # ]
    # print(solution.goodSubsetofBinaryMatrix(grid))

    # grid = [
    #     [1, 0, 0, 0, 0, 1, 0, 0]
    #     [1, 0, 1, 0, 1, 0, 1, 1]
    #     [1, 1, 0, 1, 1, 1, 1, 1]
    #     [0, 1, 1, 1, 1, 1, 0, 0]
    #     [0, 1, 0, 0, 0, 0, 0, 0]
    # ]
    # print(solution.goodSubsetofBinaryMatrix(grid))

    # grid = [
    #     [0, 0, 1, 0, 0, 1, 0, 1]
    #     [0, 1, 1, 0, 0, 0, 0, 1]
    #     [0, 0, 0, 0, 0, 0, 0, 1]
    #     [0, 0, 0, 0, 1, 1, 1, 1]
    #     [1, 0, 0, 1, 0, 1, 1, 1]
    # ]
    # print(solution.goodSubsetofBinaryMatrix(grid))
