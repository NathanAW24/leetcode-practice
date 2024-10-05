# Thought Process
`n` steps to reach top, and can climb `1` or `2` steps. How many ways to climb top?

## Case 0: `n=1` &rarr; `1` ways
`1` step = `1` steps

## Case 1: `n=2` &rarr; `2` ways
`1` step, `1` step = `2` steps
`2` step = `2` steps

## Case 2: `n=3` &rarr; `3` ways
`1` step, `1` step, `1` step = `3` steps
`2` step, `1` step = `3` steps
`1` step, `2` step = `3` steps

## Case 4: `n=4` &rarr; `5` ways
`1` step, `1` step, `1` step, 1 step = `34` steps
`2` step, `1` step, `1` step = `4` steps
`1` step, `2` step, `1` step = `4` steps
`1` step, `1` step, `2` step = `4` steps
`2` step, `2` step = `4` steps

## With induction, Case i: `n=i` &rarr; `i-1` ways + `i-2` ways

# Code
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp_arr will be <no-steps-to-top> : <no-of-ways-to-reach-top>
        dp_arr = defaultdict(int)
        dp_arr[1] = 1  # base case 1
        dp_arr[2] = 2  # base case 2

        for i in range(3, n+1):
            dp_arr[i] = dp_arr[i-1] + dp_arr[i-2]

        return dp_arr[n]
```