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
