from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # nathan

        def traverseIsland(i, j):
            # print(f"at {i},{j} ... moving")

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                # print(f"at {i},{j} ... breaking base condition")
                return

            grid[i][j] = "0"  # PAY ATTENTION to the dataype string, "0" not 0
            # problem at 0,7 it will go up even though index out of range, doesnt raise error for some reason

            if i+1 < len(grid) and grid[i+1][j] == "1":
                # print(f"go down from {i},{j}")
                traverseIsland(i+1, j)
            if j+1 < len(grid[0]) and grid[i][j+1] == "1":
                # print(f"go right from {i},{j}")
                traverseIsland(i, j+1)
            if i-1 >= 0 and grid[i-1][j] == "1":
                # print(f"go up from {i},{j}")
                traverseIsland(i-1, j)
            if j-1 >= 0 and grid[i][j-1] == "1":
                # print(f"go left from {i},{j}")
                traverseIsland(i, j-1)

            # print(f"at {i},{j} ... end")
            return

        def traverseIslandOuter(i_start, j_start):
            traverseIsland(i_start, j_start)
            print("keluar traverseIsland")

        noOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(grid[i][j])

                if grid[i][j] == "1":  # PAY ATTENTION to the dataype string, "1" not 1
                    traverseIslandOuter(i, j)
                    noOfIslands = noOfIslands + 1
                    # print(f"at {i},{j} is 1, noOfIslands {noOfIslands}")

        return noOfIslands


if __name__ == "__main__":
    solution = Solution()

    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(solution.numIslands(grid))

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(solution.numIslands(grid))
