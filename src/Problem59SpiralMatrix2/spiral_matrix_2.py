from typing import List


class Solution:

    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0 for _ in range(n)] for _ in range(n)]

        def cannotMoveRight(grid, i, j): return j + \
            1 >= len(grid[0]) or grid[i][j+1] != 0
        def cannotMoveDown(grid, i, j): return i + \
            1 >= len(grid) or grid[i+1][j] != 0

        def cannotMoveLeft(grid, i, j): return j-1 < 0 or grid[i][j-1] != 0
        def cannotMoveUp(grid, i, j): return i-1 < 0 or grid[i-1][j] != 0

        def cannotMoveAnywhere(grid, i, j): return cannotMoveRight(grid, i, j) and cannotMoveDown(
            grid, i, j) and cannotMoveLeft(grid, i, j) and cannotMoveUp(grid, i, j)

        def name(val, i, j, dir):
            grid[i][j] = val

            # base case kalo mentok ya udah cok stop traversing
            # cek mentok
            if cannotMoveAnywhere(grid, i, j):
                print(f"cannot move anywhere at {i},{j}")
                return

            # cek dir dulu
            if dir == 'r':
                if cannotMoveRight(grid, i, j):
                    print(f"cannot move right at {i},{j}, moving down")
                    name(val + 1, i + 1, j, 'd')
                else:
                    print(f"can move right at {i},{j}")
                    name(val + 1, i, j + 1, 'r')
            elif dir == 'd':
                if cannotMoveDown(grid, i, j):
                    print(f"cannot move down at {i},{j}, moving left")
                    name(val + 1, i, j - 1, 'l')
                else:
                    print(f"can move right at {i},{j}")
                    name(val + 1, i + 1, j, 'd')
            elif dir == 'l':
                if cannotMoveLeft(grid, i, j):
                    print(f"cannot move left at {i},{j}, moving up")
                    name(val + 1, i - 1, j, 'u')
                else:
                    print(f"can move right at {i},{j}")
                    name(val + 1, i, j - 1, 'l')
            elif dir == 'u':
                if cannotMoveUp(grid, i, j):
                    print(f"cannot move up at {i},{j}, moving right")
                    name(val + 1, i, j + 1, 'r')
                else:
                    print(f"can move right at {i},{j}")
                    name(val + 1, i - 1, j, 'u')

        name(1, 0, 0, 'r')
        return grid


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateMatrix(4))
