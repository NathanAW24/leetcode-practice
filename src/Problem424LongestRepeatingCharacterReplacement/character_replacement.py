from collections import defaultdict


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


s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k))

s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k))
