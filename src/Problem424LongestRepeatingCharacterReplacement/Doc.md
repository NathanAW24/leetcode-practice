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
