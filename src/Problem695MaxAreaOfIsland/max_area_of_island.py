from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # nathan

        def countIslandOuter(i_start, j_start):
            global localmax
            localmax = 0

            def countIsland(i, j):
                global localmax
                print(f"at {i},{j} ... moving")

                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                    print(f"at {i},{j} ... breaking base condition")
                    return
                # grid[i][j] = 0
                # localmax = localmax + 1
                grid[i][j] = 0
                # problem at 0,7 it will go up even though index out of range, doesnt raise error for some reason
                localmax = localmax + 1
                if i+1 < len(grid) and grid[i+1][j] == 1:
                    print(f"go down from {i},{j}")
                    countIsland(i+1, j)
                if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                    print(f"go right from {i},{j}")
                    countIsland(i, j+1)
                if i-1 >= 0 and grid[i-1][j] == 1:
                    print(f"go up from {i},{j}")
                    countIsland(i-1, j)
                if j-1 >= 0 and grid[i][j-1] == 1:
                    print(f"go left from {i},{j}")
                    countIsland(i, j-1)

                print(f"at {i},{j} ... end")
                return
            countIsland(i_start, j_start)
            return localmax

        maxValue = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(grid[i][j])

                if grid[i][j] == 1:
                    oneIslandMax = countIslandOuter(i, j)
                    print(f"island at {i},{j}, size is {oneIslandMax}")
                    if oneIslandMax > maxValue:
                        maxValue = oneIslandMax

        return maxValue


if __name__ == "__main__":
    solution = Solution()

    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
        0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(solution.maxAreaOfIsland(grid))

    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    print(solution.maxAreaOfIsland(grid))
