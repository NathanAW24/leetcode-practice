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
