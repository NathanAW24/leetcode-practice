# Problems
## Problem 1: Code doesn't skip non-alphanumerical characters
With this code
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s)-1

        while left_pointer < right_pointer:
            if not s[left_pointer].isalnum():
                left_pointer += 1
            if not s[right_pointer].isalnum():
                right_pointer -= 1

            if s[left_pointer].lower() != s[right_pointer].lower():
                print(left_pointer, s[left_pointer],
                      right_pointer, s[right_pointer])
                return False

            left_pointer += 1
            right_pointer -= 1

        return 
        
s = "A man, a plan, a canal: Panama"
# true bcs "amanaplanacanalpanama" is palindrome
print(Solution().isPalindrome(s))
```

This gives log of
```
6   25 a
False
```

The reason it happened is because, when `left_pointer` is getting the index of the `","` after `"...man..."`, it now points to `" "`, there's no further iteration to filter the character again whether it is `.alnum()` or not. So the fix is to add `continue` after we add or subtract the value of the `left_pointer` or `right_pointer`.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s)-1

        while left_pointer < right_pointer:
            if not s[left_pointer].isalnum():
                left_pointer += 1
                continue # ADD HERE
            if not s[right_pointer].isalnum():
                right_pointer -= 1
                continue # ADD HERE

            if s[left_pointer].lower() != s[right_pointer].lower():
                print(left_pointer, s[left_pointer],
                      right_pointer, s[right_pointer])
                return False

            left_pointer += 1
            right_pointer -= 1

        return True
```

With this, we made it check again if the next character is also `isalnum()` or not, this will truly only allow alphanumeric characters to be checked.

# Neetcode Solution
Same logic but slightly different execution.
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s)-1

        while left_pointer < right_pointer:
            while left_pointer < right_pointer and not s[left_pointer].isalnum():
                left_pointer += 1
            while right_pointer > left_pointer and not s[right_pointer].isalnum():
                right_pointer -= 1

            if s[left_pointer].lower() != s[right_pointer].lower():
                return False

            left_pointer += 1
            right_pointer -= 1

        return True
```

Instead of using `if` statements to check whether it is alphanumerical, which makes it need to re-run the outer `while` loop from the very beginning, this one captures the need to re-run the `isalnum()` check within an inner `while` loop itself.