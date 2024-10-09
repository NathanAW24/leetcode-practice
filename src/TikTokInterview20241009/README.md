# Interview Process

## Question 1
First, he asked me to introduce myself, then I introduce myself with slides. When I was showing off hungrybees, he asked me about `RecyclerView`, how did I do it. Like if I was rendering a very long list (10k entries), how do I make the performance optimized, since its gonna take very long, to render everything. REVIEW MORE ON THIS.

The second mobile phone there.
![alt text](image.png)

## Question 2
Given a string `"abcd-e-f"` reverse the string but keep the dashes (or non-letters) there. So the reverse string here will be `"fedc-b-a"`. Basically this [leetcode question](https://leetcode.com/problems/reverse-vowels-of-a-string/description/) with additional modif.

Solution uses two pointer, then always do check for values at both pointers
- `s[l]` and `s[r]` are letters (`<some-character>.isalpha()`) &rarr; `switch s[l] and s[r]`; `move l+=1`, `move r-=1`
- `s[l]` letter, `s[r]` not letter &rarr; `move r-=1`
- `s[l]` not letter, `s[r]` letter &rarr; `move l+=1`
- `s[l]` and `s[r]` not letters &rarr; `move r-=1`, `move l+=1`

This is the code I wrote with some test cases in mind, in `src/TikTokInterview20241009/main.py`.
```python
def reverse_string(s):
    s = list(s)
    l, r = 0, len(s)-1

    while l <= r:  # pointer is not colliding

        # first case 1: s[l] and s[r] are characters
        if s[l].isalpha() and s[r].isalpha():
            # switch s[l] and s[r]
            temp = s[l]
            s[l] = s[r]
            s[r] = temp

            l += 1
            r -= 1
            continue
        elif not s[r].isalpha() and s[l].isalpha():
            # let it be
            r -= 1
        elif not s[l].isalpha() and s[r].isalpha():
            # let it be
            l += 1
        else:
            # let it be
            r -= 1
            l += 1

    return ''.join(s)


s1 = "abcd-e-f"
print(reverse_string(s1))  # fedc-b-a

s2 = "e-abc-d"
print(reverse_string(s2))  # d-cba-e
```


He finally asked, if there was any other test case I can consider. For this, maybe should consider some more edge cases.

Asked chatgpt if code is correct? and for some additional test cases?
```python
...
# Original Test Cases
s1 = "abcd-e-f"
print(reverse_string(s1))  # Output: "fedc-b-a"

s2 = "e-abc-d"
print(reverse_string(s2))  # Output: "d-cba-e"

# Additional Test Cases

# 1. Empty String
s_empty = ""
print(reverse_string(s_empty))  # Output: ""

# 2. All Letters
s_all_letters = "abcdef"
print(reverse_string(s_all_letters))  # Output: "fedcba"

# 3. All Non-Letters
s_all_non_letters = "----"
print(reverse_string(s_all_non_letters))  # Output: "----"

# 4. Single Character
s_single_letter = "a"
print(reverse_string(s_single_letter))  # Output: "a"

s_single_non_letter = "-"
print(reverse_string(s_single_non_letter))  # Output: "-"

# 5. Multiple Non-Letters in a Row
s_multiple_non_letters = "a--b--c"
print(reverse_string(s_multiple_non_letters))  # Output: "c--b--a"

# 6. Starting and Ending with Non-Letters
s_start_end_non_letters = "-a-b-"
print(reverse_string(s_start_end_non_letters))  # Output: "-b-a-"

# 7. Mixed Cases
s_mixed_cases = "a-Bc-D"
print(reverse_string(s_mixed_cases))  # Output: "D-cB-a"

# 8. Unicode Characters
s_unicode = "a-ß-c"
print(reverse_string(s_unicode))  # Output: "c-ß-a"

# 9. Letters and Numbers
s_letters_numbers = "a1b2c3"
print(reverse_string(s_letters_numbers))  # Output: "c1b2a3"

# 10. Letters and Symbols
s_letters_symbols = "a!b@c#"
print(reverse_string(s_letters_symbols))  # Output: "c!b@a#"

# 11. Spaces Included
s_with_spaces = "a - b -c"
print(reverse_string(s_with_spaces))  # Output: "c - b -a"

# 12. Long String with Multiple Non-Letters
s_long = "a-bC-dEf-ghIj"
print(reverse_string(s_long))  # Output: "j-Ih-gfE-dCba"
```

# Personal Feedback
Review your project deeply, you should know everything deeply about your project that you show.