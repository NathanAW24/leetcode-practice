# Thought Process
## First Thought
From these three cases
```
[3, 4, 5, 1, 2]
          ^
       smallest: index = 3 = 2 + 1 = 5 // 2 + 1(rounddown division) = len(nums) // 2 + 1

[4, 5, 6, 7, 0, 1, 2]
          ^
       same as above

[11, 13, 15, 17]
 ^
smallest, index = 0 = first index

```

So we take the `index=len(nums)//2`, check if `nums[index+1] > nums[index]`
- YES, means that array is not rotated ==> return `nums[0]`
- NO, means array is rotated ==> return `nums[len(nums)//2 + 1]`

OK Turns out that is wrong, rotate doesnt mean anyhow move, 1 rotation means moving every element one step to the right.

## Second Thought
```
3 4 5 1 2
^       ^
l       r
```

First property noticed, a normal array would be `1 2 3 4 5 ...` with values ascending, so we can check the ends of the array `l` and `r` pointer(or subsequent subarrays) to check if there's inflection. If `nums[l] > nums[r]`, then there is an inflection in between. There won't be an inflection if it maintains the order of `nums[l] < nums[r]`.

So first thing to do is, check if there's an inflection.
```
3 4 5 1 2
^       ^
l       r
```
`nums[l]=3 > nums[r]=2` &rarr; means there's an inflection somewhere in the middle.

We find the `mid=r//2`.
```
3 4 5 1 2
^   ^   ^
l  mid  r
```

Now how to decide where to move? Let's take a look at some other cases as well.
- Inflection point at the right hand side, how to detect? `nums[mid] > nums[r]` &rarr; `mid=l`
```
3 4 5 6 7 1 2
^     ^     ^
l    mid    r
```
check if mid is the inflection point or not (inflection point will only be on the right of mid). `nums[mid] > nums[mid+1]`? NO. `nums[mid-1] > nums[mid]`? NO. Then, `continue`.

Go through same process
```
3 4 5 6 7 1 2
      ^ ^    ^
      l mid  r
```
check if mid is the inflection point or not (inflection point will only be on the right of mid). `nums[mid] > nums[mid+1]`? YES, the return `nums[mid+1]`

- Inflection point at the left hand side, how to detect? `nums[l] > nums[mid]` &rarr; `mid=r`
```
7 1 2 3 4 5 6
^     ^     ^
l    mid    r
```

```
7 1 2 3 4 5 6
^ ^   ^
l mid r    
```
Another similar case
```
6 7 1 2 3 4 5 
^ ^   ^
l mid r    
```
So we need to check both, if nums[mid] is the minimum, or nums[mid+1] is the minimum.
- nums[mid] > nums[mid+1] &rarr; return nums[mid+1]
- nums[mid-1] > nums[mid] &rarr; return nums[mid]


# Scribbles
## Scribble 1
```
3 4 5 6 7 1 2
      ^ ^    ^
      l mid  r
```

```
3 4 5 6 7 1 2
        ^ ^ ^
        l m r
```

`mid=(r-l)//2 + l` 
```
3 4 5 6 7 1 2
        ^ ^r
        l,m
```

Will `mid` always fall at `l`? Such that minimal point is at `mid+1`, can it be

## Scribble 2
```
7 8 1 2
^ ^   ^
l m   r
```
`mid=3-0//2 + 0 = 1`
since `nums[mid] > nums[right]` &rarr; choose right
`mid = l`


```
7 8 1 2
  ^ ^ ^
  l m r
```
`mid=3-1//2 + 1 = 2`
since `nums[l] > nums[mid]` &rarr; choose left
`mid=r`

```
7 8 1 2
  ^ ^r
  l,m
```
`mid = 2-1//2 + 1 = 1`
since `l == mid` &rarr; inflection point found at `nums[mid+1]`

# My Solution (Without Looking at Neetcode)
## Generalization From Scribbles
So from scribbles above, I can find out that, if there's an inflection within the array, we can keep doing binary search until we find that `l` and `r` is side by side, like example below
```
7 8 1 2
  ^ ^r
  l,m
```

This makes the `mid == l`, after calculating for new `mid=(r-l)//2 + l` and would be the base case that breaks the scenario. It will place `l` (and `mid`), at the highest point, and `r` (or `mid+1` or `l+1`), the lowest point (between `l` and `r` is the inflection).

## Code
So here's the code
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1
        mid = (r-l)//2 + l

        if len(nums) == 1:
            return nums[0]  # smallest number be the only number itself

        if nums[l] < nums[r]:
            return nums[0]

        while l != mid:
            if nums[l] > nums[mid]:
                # choose left
                r = mid
            elif nums[mid] > nums[r]:
                l = mid

            mid = (r-l)//2 + l

            print(f"l, mid, r: {l, mid, r}")

        return nums[l+1]
```

This is quite generic and elegant, with least amount of checks.