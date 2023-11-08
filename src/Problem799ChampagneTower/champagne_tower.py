class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # init the array
        cup = [[0 for j in range(i + 1)] for i in range(query_row + 1)]

        # if cup[i][j] > 1 ==> cup[i + 1][j] += 1/2 * (cup[i][j] - 1); cup[i + 1][j + 1] += 1/2 * (cup[i][j] - 1)

        cup[0][0] = poured

        for i in range(query_row + 1):
            for j in range(i + 1):
                if cup[i][j] > 1:
                    excess = cup[i][j] - 1

                    cup[i][j] = 1
                    try:
                        cup[i + 1][j] = cup[i + 1][j] + 1/2 * excess
                        cup[i + 1][j + 1] = cup[i + 1][j + 1] + 1/2 * excess
                    except:
                        print("out of range index")
                print(f"at cup {i},{j} the value is {cup[i][j]}")

        return cup[query_row][query_glass]


if __name__ == "__main__":
    solution = Solution()

    query_row = 4
    query_glass = 2
    result = solution.champagneTower(100, query_row, query_glass)
    print(f"The cup cup[{query_row},{query_glass}] value is : {result}")
