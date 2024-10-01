from collections import defaultdict


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


s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k))

s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k))
