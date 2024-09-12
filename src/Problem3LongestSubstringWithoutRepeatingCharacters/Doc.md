# Problems
## Problem 1: O(n^2) solution
Although my code is accepted, but I understand that it is not the most optimized solution I can do.
```python
class Solution:  # NOT MOST OPTIMIZED, BUT AC IN 8 mins
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        for i in range(len(s)):
            inner_hash = set()
            length = 0
            for j in range(i, len(s)):
                if s[j] not in inner_hash:
                    length += 1
                    inner_hash.add(s[j])
                else:
                    break
            maxlength = max(maxlength, length)

        return maxlength


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
```

It takes `O(n^2)` time and `O(1)` space. Solution is instead of doing this kind of iteration, we use sliding window, we shrink the substring of the subarray once we find a duplicate letter. Straight to neetcode solution.

## Problem 2: Keeping `length` variable
```python
class Solution:  # NOT MOST OPTIMIZED, BUT AC IN 8 mins
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        left_pointer = 0
        maxlength = 0

        for right_pointer in range(len(s)):
            length = maxlength
            while s[right_pointer] in hash:
                hash.remove(s[left_pointer])
                left_pointer += 1
                length -= 1

            hash.add(s[right_pointer])
            length += 1
            maxlength = max(maxlength, length)

        return maxlength
```

This is an inaccurate way to maintain the `length` variable. The length value never depends on maxlength, but it depends on how big the substring of the sliding window is. So here is where it should be placed.
```python
class Solution:  # NOT MOST OPTIMIZED, BUT AC IN 8 mins
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        left_pointer = 0
        maxlength = 0
        length = 0 ### HERE

        for right_pointer in range(len(s)):
            ### NO NEED FOR assigning, length = maxlength
            while s[right_pointer] in hash:
                hash.remove(s[left_pointer])
                left_pointer += 1
                length -= 1

            hash.add(s[right_pointer])
            length += 1
            maxlength = max(maxlength, length)

        return maxlength
```

# Neetcode Solution
The key for understanding neetcode solution, is keeping two pointers, `left_pointer` and `right_pointer`, to keep track of the start and end of the substring. We need to keep iterating `right_pointer` from start to finish, but once we found a duplicate, we have to move `left_pointer` forward until there's no longer any duplicate. As we move the `left_pointer` forward, keep in mind that we need to remove the letter from the `hash` as well, since it only contains all the unique letters within the substring. Keep in mind that we also need to keep checking the length of the substring, each time new substring is formed, to keep track of the maximum.

Here's the TODO
1. Instantiate `hash = set()` and `l=0`, create the set and left pointer.
2. Iterate over `0` to `n`, for `right_pointer` right pointer.
    - While `s[right_pointer]` right pointer letter is in `hash`, we want to shrink the substring by moving the `left_pointer` left pointer forward and removing `s[left_pointer]` since the `hash` only contains unique letters available in the substring, also do `length-=1` to reduce the length of the substring.
    - Previous step will remove all duplicates, now after removing all duplicates, we only need to add `s[right_pointer]` to the substring (add inside `hash`), and `length+=1`
    - Then compare for `maxlength = max(maxlenth, length)`
3. return `maxlength` at the end

This is my interpretation of neetcode solution
```python
class Solution:  # NOT MOST OPTIMIZED, BUT AC IN 8 mins
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        left_pointer = 0
        maxlength = 0
        length = 0

        for right_pointer in range(len(s)):
            while s[right_pointer] in hash:
                hash.remove(s[left_pointer])
                left_pointer += 1
                length -= 1

            hash.add(s[right_pointer])
            length += 1
            maxlength = max(maxlength, length)

        return maxlength
```

Neetcode's solution is similar, but slightly different in a way, as he does not keep track of `length` variable, he calculates the length on each iteration with `right_pointer + 1 - left_pointer`, which is the same as `<length-of-string-from-0-to-right_pointer> - <length-of-string-before-sliding-window>`, this gives the same length of sliding window substring.
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        left_pointer = 0
        maxlength = 0

        for right_pointer in range(len(s)):
            while s[right_pointer] in hash:
                hash.remove(s[left_pointer])
                left_pointer += 1

            hash.add(s[right_pointer])
            maxlength = max(maxlength, right_pointer + 1 - left_pointer)

        return maxlength
```

Overall similar logic.