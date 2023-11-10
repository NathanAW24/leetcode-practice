# Good Subset of a Binary Matrix

You are given a 0-indexed `n x m` binary matrix `grid`, you want to choose a subset of rows such that the sum of each column is at most half of the length of the subset.

For example,

```plaintext
grid = [
  [0, 1, 0],
  [1, 1, 1],
  [1, 0, 0],
  [0, 0, 0],
]
```
We can choose a subset with row 0 and row 2.
```plaintext
subset = [0, 2]
grid[0] = [0, 1, 0]
grid[2] = [1, 0, 0]
sums    = [1, 1, 0]
```
Each element in array `sums` is at most half of `length(subset) = 2`.

Find any valid subset of rows and return their row indexes as an integer array. You can return them in any order. If there is no such subset, return an empty array.


## Function Description
Complete the function `gridSubset` in the editor below. The function returns a single integer array.

`gridSubset` has the following parameter(s):

`grid`: an `n x m` 2D binary matrix.

## Constraints
`1 < n <= 2 * 10^5`.
`1 <= m <= 8`.
For `0 <= i < n` and `0 <= j < m`, `grid[i][j]` is `0` or `1`.

## Input Format For Custom Testing

The first line contains an integer, `n`, denoting the number of rows in `grid`.
The second line contains an integer, `m`, denoting the number of columns in grids in `grid`.
Each line `i` of the `n` subsequent lines (where `0 <= i < n`) contains `m` integers.

### Sample Case 0
**Sample Input For Custom Testing**
```plaintext
3
4
0 0 1 0
1 1 1 1
1 0 0 0
```
**Sample Output**
```plaintext
0
2
```
**Explanation**
```plaintext
subset = [0, 2]
grid[0] = [0, 1, 0]
grid[2] = [1, 0, 0]
sums    = [1, 1, 0]
```

### Sample Case 1
**Sample Input For Custom Testing**
```plaintext
3
3
0 0 0
0 0 1
1 0 0
```
**Sample Output**
```plaintext
0
1
2
```
**Explanation**
```plaintext
subset = [0, 1, 2]
grid[0] = [0, 0, 0]
grid[1] = [0, 0, 1]
grid[2] = [1, 0, 0]
sums    = [1, 0, 1]
```