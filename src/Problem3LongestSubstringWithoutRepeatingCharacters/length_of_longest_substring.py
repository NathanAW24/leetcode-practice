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
