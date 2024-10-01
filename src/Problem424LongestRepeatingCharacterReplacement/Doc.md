# Thought Process
## First case, `"ABAB", k=2`
Don't forget to keep track of the longest_string

ABAB
^^
lr
hash = {A: 1, B: 1}, k_used = 1
max hash --> A or B same, the rest change to max hash

ABAB
^ ^
l r
hash = {A: 2, B: 1}, k_used = 1 + 0 = 1
max hash --> A, the rest change to max hash

ABAB
^  ^
l  r
hash = {A: 2, B: 2}, k_used = 1 + 1 = 2 >= 2
max hash --> A, the rest change to max hash
since k_used >= 2 --> move l --> revert k_used = 0

ABAB
 ^ ^
 l r
hash = {A: 1, B: 2}, k_used = 0 + 1 = 1
max hash --> B, the rest change to max hash

move r, but cannot so move l --> revert k_used = 0 (?)
ABAB
  ^^
  lr
hash = {A: 1, B: 1}, k_used = 1 + 0 = 1
max hash --> A or B same, the rest change to max hash

Return maximum string

BIG QUESTION: When do we move the `l` pointer? Do we need to move `r` left?

## Second case, `"AABABBA", k=1`

AABABBA
^^
lr
hash = {A:2}, k_used = 0
max hash --> A, no changes needed
max_length = 2

AABABBA
^ ^
l r
hash = {A:2, B:1}, k_used = 0 + 1 = 1 --> cara hitungnya bukan gini, tapi pake `total(hash) - hash[max_val]`
max hash --> A, change the rest to A
max_length = 3

AABABBA
^  ^
l  r
hash = {A:3, B:1}, k_used = 1 + 0 = 1
max hash --> A, change the rest to A
max length = 4

AABABBA
^   ^
l   r
hash = {A:3, B:2}, k_used = 1 + 1 = 2 > k --> need to change 2 B's to A's
max hash --> A, change the rest to A
move left

AABABBA
 ^  ^
 l  r
hash = {A:2, B:2}, k_used = 2 > k --> need to change 2 B's to A's
max hash --> A or B same, change the rest
move left

AABABBA
  ^ ^
  l r
hash = {A:1, B:2}, k_used = 1 == k --> need to change 1 A to B.
max hash --> B, change the rest
move right again

AABABBA
  ^  ^
  l  r
hash = {A:1, B:2}, k_used = 1 == k --> need to change 1 A to B.
max hash --> B, change the rest
move right again

AABABBA
  ^   ^
  l   r
hash = {A:2, B:3}, k_used = 2 > k --> need to change 2 A's to B's
max hash --> 

# Problems
## Problem 1: Handle hash incorrectly
In this line
```python
...
        hash[l] += 1
...
```

I am using the index to put into the hash, meanwhile I should be using `s[l]`. Happens on other instances as well for `r` also.
```python
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        hash = defaultdict(int)  # hash contains { letter : appearance }

        max_len = 0

        if len(s) == 1:
            return 1

        # first set of characters input to hash
        hash[l] += 1

        k_used = 0

        while r < len(s)-1:
            hash[r] += 1
            values_arr = hash.values()

            # hitung `total(hash) - hash[max_val]`
            k_used = sum(values_arr) - max(values_arr)

            while k_used > k:
                hash[l] -= 1
                l += 1
                hash[l] += 1

            r += 1

            max_len = max(max_len, r + 1 - l)

        return max_len
```

Fix it to this
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        hash = defaultdict(int)  # hash contains { letter : appearance }

        max_len = 0

        if len(s) == 1:
            return 1

        # first set of characters input to hash
        hash[s[l]] += 1

        k_used = 0

        while r <= len(s)-1:
            hash[r] += 1
            values_arr = hash.values()

            # hitung `total(hash) - hash[max_val]`
            k_used = sum(values_arr) - max(values_arr)

            while k_used > k:
                hash[s[l]] -= 1
                l += 1
                hash[s[l]] += 1

            r += 1

            max_len = max(max_len, r + 1 - l)

        return max_len
```

## Problem 2: Redundant addtition of hash
This section
```python
...
            while k_used > k:
                hash[s[l]] -= 1
                l += 1
                hash[s[l]] += 1
...
```

within
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        hash = defaultdict(int)  # hash contains { letter : appearance }

        max_len = 0

        if len(s) == 1:
            return 1

        # first set of characters input to hash
        hash[s[l]] += 1

        k_used = 0

        while r <= len(s)-1:
            hash[r] += 1
            values_arr = hash.values()

            # hitung `total(hash) - hash[max_val]`
            k_used = sum(values_arr) - max(values_arr)

            while k_used > k:
                hash[s[l]] -= 1
                l += 1
                hash[s[l]] += 1

            r += 1

            max_len = max(max_len, r + 1 - l)

        return max_len
```

Must be changed to remove
```python
...
                hash[s[l]] += 1
...
```

As this addition of that specific letter is added by the `s[r]` already.

## Problem 3: `sum(values_arr)` is basically length `r + 1 - l`, no need to use `sum(hash.values())`
```python
...
            # hitung `total(hash) - hash[max_val]`
            k_used = sum(values_arr) - max(values_arr)
...
```

Can just change to
```python
...
            # hitung `total(hash) - hash[max_val]`
            k_used = r + 1 - l - max(values_arr)
...
```

## Problem 4: `max_len = max(max_len, r + 1 - l)` kebalik dengan `r += 1`
```python
...
            r += 1
            max_len = max(max_len, r + 1 - l)
...
```

Should be
```python
...
            max_len = max(max_len, r + 1 - l)
            r += 1
...
```
Makes sense coz, we should evaluate length at current before adding the length.

With problem 3 and 4, it becomes 
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        hash = defaultdict(int)  # hash contains { letter : appearance }

        print(s)

        max_len = 0

        if len(s) == 1:
            return 1

        # first set of characters input to hash
        hash[s[l]] += 1

        k_used = 0

        while r <= len(s)-1:
            hash[r] += 1

            values_arr = hash.values()

            # hitung `total(hash) - hash[max_val]`
            k_used = r + l - 1 - max(values_arr)

            while k_used > k:
                print(l, s[l])
                hash[s[l]] -= 1
                l += 1

            r += 1
            max_len = max(max_len, r + 1 - l)

        return max_len
```

## Problem 5: `k_used` needs to be recalculated again when `l+=1`
Within this code
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        hash = defaultdict(int)  # hash contains { letter : appearance }

        print(s)

        max_len = 0

        if len(s) == 1:
            return 1

        # first set of characters input to hash
        hash[s[l]] += 1

        k_used = 0

        while r <= len(s)-1:
            hash[r] += 1

            values_arr = hash.values()

            # hitung `total(hash) - hash[max_val]`
            k_used = r + l - 1 - max(values_arr)

            while k_used > k:
                print(l, s[l])
                hash[s[l]] -= 1
                l += 1

            r += 1
            max_len = max(max_len, r + 1 - l)

        return max_len

```

This part 
```python
...
            while k_used > k:
                print(l, s[l])
                hash[s[l]] -= 1
                l += 1
...
```

`k_used` value should change after `l+=1`, so need to recalculate again.
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        hash = defaultdict(int)  # hash contains { letter : appearance }

        print(s)

        max_len = 0

        if len(s) == 1:
            return 1

        # first set of characters input to hash
        hash[s[l]] += 1

        k_used = 0

        while r <= len(s)-1:
            hash[r] += 1

            # hitung `total(hash) - hash[max_val]`
            k_used = r - l + 1 - max(hash.values())

            while k_used > k:
                print(l, s[l])
                hash[s[l]] -= 1
                l += 1
                k_used = r - l + 1 - max(hash.values())

            r += 1
            max_len = max(max_len, r - l + 1)

        return max_len
```

## Probelm 6: Gak teliti 
fix `hash[r]` to `hash[s[r]]`

## Problem 7: Flip back `max_len` and `r+=1`
This should be it, turns out, max_len done before r+=1 in this case.
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        hash = defaultdict(int)  # hash contains { letter : appearance }

        print(s)

        max_len = 0

        if len(s) == 1:
            return 1

        # first set of characters input to hash
        hash[s[l]] += 1

        k_used = 0

        while r <= len(s)-1:
            hash[s[r]] += 1

            # hitung `total(hash) - hash[max_val]`
            k_used = r - l + 1 - max(hash.values())

            while k_used > k:
                print(l, s[l])
                hash[s[l]] -= 1
                l += 1
                k_used = r - l + 1 - max(hash.values())

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
```

# Neetcode Solution
So basically neetcode logic and mine is the same already. With mainly moving the `r` pointer, and only moving the `l` pointer when `<number-of-words-to-replace> > k`, or here it is `k_used`. But, to optimize speed and memory for `k_used`, we do not need to count the `max(hash.values())`. This operation itself makes it complex in memory and space.

## How do we optimize for `max(hash.values())`?
Instead of counting for `max(hash.values())`, we just need to count the `<maximum-count-of-identical-letters-ever-seen-in-the-loop>` denoted by `max_count` (or `maxf` in neetcode's solution), instead of `<maximum-count-of-identical-letters-within-current-hash>` denoted by `max(hash.values())`.

We don't need to re-scan the entire `hash` to find which has the highest `count` or frequency in each iteration, it is `O(26)`.

Result would only be maximized as we find a new max frequency `max_count`. If we were to find a new `max_len` within the new string `s`, we would need to find a new `max_count` which will then maximize the `max_len` as well. 

For example (with `k=1`), when the substring in the window is `"AABAA"`, then `max_count` is `4`. If we find another case where `"ABAA"` for some reason, the `max(hash.values())` would give `3`, but the potential substring here, pasti bukan substring paling panjang, that can update `max_len`, as the `max_len` will be equivalent to `max(hash.values()) + k` giving `5`, padahal previous iteration ada `6`. That means, these cases where `max(hash.values())` decrease, can be skipped. The next possible substring that can update `max_len` needs to at least have `max(hash.values())` to be `> 4`, then can lebih besar dari `max_len`, yang tadinya `6` jadi `> 6`. 

So what we do here is just keep a variable `max_count` to keep track of `<maximum-count-of-identical-letters-ever-seen-in-the-loop>`, ever seen by all the substrings, previously appointed as the longest, with `max_len`. We do this by `max_count = max(max_count, hash[s[r]])`, as every time we add a new `s[r]`, letter with `r` pointer, we might be finding a new `max_count`, just from this new appointed substring from `l` to `r` inclusively.

Then `k_used > k` accordingly will skip some of the substrings that are confirm not longer than `max_len`.

## Concrete example of the last statement
### With `max(hash.values())`, `s="AAABB..."`, `k=1`

```
AAABB...
^^
lr
```

```
AAABB...
^ ^
l r
```

```
AAABB...
^  ^
l  r
```

```
AAABB...
^   ^
l   r
```
This will trigger `length - max(hash.values()) > k`, and move `l` pointer

```
AAABB...  
 ^  ^
 l  r
```

```
AAABB...  
  ^ ^
  l r
```
until it reaches this point, then continue doing the normal calculation again, moving `r` pointer.

### With `max_count`, `s="AAABB..."`, `k=1`
```
AAABB...
^^
lr
```
`max_count` update to `2`

```
AAABB...
^ ^
l r
```
`max_count` update to `3`

```
AAABB...
^  ^
l  r
```
`max_count` stays at `3`

```
AAABB...
^   ^
l   r
```
`max_count` stays at `3`
This will trigger `length - max_count > k` (`5-3 > 1`), and move `l` pointer.

```
AAABB...  
 ^  ^
 l  r
```
However, it will stop here, since `length - max_count > k` (`4-3 !> 1`) no longer triggered, and it will continue the normal calculation again, moving `r`.

## Code
Here's the code, my interpretation
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        hash = defaultdict(int)  # hash contains { letter : appearance }

        print(s)

        max_len = 0
        max_count = 0

        if len(s) == 1:
            return 1

        # first set of characters input to hash
        hash[s[l]] += 1

        k_used = 0

        while r <= len(s)-1:
            hash[s[r]] += 1

            # hitung `total(hash) - hash[max_val]`
            max_count = max(max_count, hash[s[r]])
            k_used = r - l + 1 - max_count

            while k_used > k:
                brp_kali_masuk += 1
                hash[s[l]] -= 1
                l += 1
                k_used = r - l + 1 - max_count

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
```

A bit neater would be
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        hash = defaultdict(int)  # hash contains { letter : appearance }

        print(s)

        max_len = 0
        max_count = 0

        if len(s) == 1:
            return 1

        # first set of characters input to hash
        hash[s[l]] += 1

        while r <= len(s)-1:
            hash[s[r]] += 1

            max_count = max(max_count, hash[s[r]])

            while r - l + 1 - max_count > k:
                hash[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
```